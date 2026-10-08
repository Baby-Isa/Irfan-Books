-- Pandoc Lua filter: Markdown conventions → raw Typst calls into build/template.typ
--   ::: {.box-word title="..."} … :::   → #callout(kind: "word", title: "...")[…]
--   ::: {.ayah ref="30:21"} translation ::: → #ayah(ref:, arabic: <from sources/quran>)[…]
--   [نص]{lang=ar}                         → #ar[…]
-- Quranic Arabic is ALWAYS inserted here from the verified text, never typed by hand.

local quran = nil
local function load_quran()
  if quran then return quran end
  quran = {}
  local root = os.getenv("IRFAN_ROOT") or "."
  local f = assert(io.open(root .. "/sources/quran/quran-uthmani.tsv", "r"))
  for line in f:lines() do
    if line:sub(1, 1) ~= "#" then
      local s, a, t = line:match("^(%d+)\t(%d+)\t(.*)$")
      if s then quran[s .. ":" .. a] = t end
    end
  end
  f:close()
  return quran
end

local function verses(ref)
  -- "30:21" or "30:21-22"
  local s, a, b = ref:match("^(%d+):(%d+)%-?(%d*)$")
  if not s then error("bad ayah ref: " .. ref) end
  local q, out = load_quran(), {}
  for i = tonumber(a), tonumber(b ~= "" and b or a) do
    local t = q[s .. ":" .. i]
    if not t then error("ayah not found: " .. s .. ":" .. i) end
    local d = tostring(i):gsub("%d", function(c) return utf8.char(0x0660 + tonumber(c)) end)
    table.insert(out, t .. " ﴿" .. d .. "﴾")
  end
  return table.concat(out, " ")
end

local function tstr(s) -- Typst string literal
  return '"' .. s:gsub('\\', '\\\\'):gsub('"', '\\"') .. '"'
end

local kinds = { word = true, history = true, story = true, who = true, reflect = true, try = true }

function Div(el)
  for _, cls in ipairs(el.classes) do
    local kind = cls:match("^box%-(%a+)$")
    if kind and kinds[kind] then
      local title = el.attributes.title
      local open = "#callout(kind: " .. tstr(kind) .. (title and (", title: " .. tstr(title)) or "") .. ")["
      local blocks = { pandoc.RawBlock("typst", open) }
      for _, b in ipairs(el.content) do table.insert(blocks, b) end
      table.insert(blocks, pandoc.RawBlock("typst", "]"))
      return blocks
    end
    if cls == "point" then
      -- review note for the user (D30): shown in drafts, dropped from --final builds
      if os.getenv("IRFAN_FINAL") == "1" then return {} end
      local blocks = { pandoc.RawBlock("typst", "#point[") }
      for _, b in ipairs(el.content) do table.insert(blocks, b) end
      table.insert(blocks, pandoc.RawBlock("typst", "]"))
      return blocks
    end
    if cls == "words" then
      local blocks = { pandoc.RawBlock("typst", "#words[") }
      for _, b in ipairs(el.content) do table.insert(blocks, b) end
      table.insert(blocks, pandoc.RawBlock("typst", "]"))
      return blocks
    end
    if cls == "ayah" then
      local ref = el.attributes.ref or error("ayah div needs ref=")
      local open = "#ayah(ref: " .. tstr(ref) .. ", arabic: " .. tstr(verses(ref)) .. ")["
      local blocks = { pandoc.RawBlock("typst", open) }
      for _, b in ipairs(el.content) do table.insert(blocks, b) end
      table.insert(blocks, pandoc.RawBlock("typst", "]"))
      return blocks
    end
  end
end

function Span(el)
  if el.attributes.lang == "ar" then
    local inl = { pandoc.RawInline("typst", "#ar[") }
    for _, i in ipairs(el.content) do table.insert(inl, i) end
    table.insert(inl, pandoc.RawInline("typst", "]"))
    return inl
  end
end

-- Drop HTML comments (src traces) from typeset output.
function RawBlock(el) if el.format == "html" then return {} end end
function RawInline(el) if el.format == "html" then return {} end end

-- Citations → footnotes (D21). [@key, locator] becomes a footnote "Short form, locator."
-- Add a line here whenever a key is added to sources/bibliography.bib.
local SHORT = {
  nahj = "Imam ʿAli, *Nahj al-Balagha* (trans. Qutbuddin)",
  sahifa = "Imam Zayn al-ʿAbidin, *al-Sahifa al-Sajjadiyya* (trans. Chittick)",
  mafatih = "Shaykh ʿAbbas Qummi, *Mafatih al-Jinan*",
  kernel = "ʿAllama Tabatabaʾi and S. M. H. Husayni Tihrani, *Kernel of the Kernels* (trans. Qaraʾi)",
  light = "Mutahhari, Tabatabaʾi and Khomeini, *Light Within Me*",
  journey = "Mirza Jawad Maliki Tabrizi, *The Spiritual Journey of the Mystics*",
  forty_hadith = "Imam Khomeini, *Forty Hadith*",
  inner_secrets = "Sayyid Haydar Amuli, *Inner Secrets of the Path*",
  lantern = "*Lantern of the Path* (Misbah al-Shariʿa)",
  self_knowledge = "Mohammad Ali Shomali, *Self-Knowledge*",
  qarai = "*The Qurʾan*, trans. ʿAli Quli Qaraʾi",
  bahmanpour_slides = "M. S. Bahmanpour, lecture slides",
  duas_munajat_shabaniyah = "*Munajat Shaʿbaniyyah* (duas.org)",
  duas_dua_kumayl = "*Duʿa Kumayl* (duas.org)",
  duas_ramadan_dua_abu_hamza_thumali = "*Duʿa Abu Hamza al-Thumali* (duas.org)",
  duas_dua_arafah_imam_husain = "Imam al-Husayn, *Duʿa ʿArafah* (duas.org)",
  duas_salat_al_layl_tahajjud_prayer = "*Salat al-Layl* (duas.org)",
}
function Cite(el)
  local parts = {}
  for _, c in ipairs(el.citations) do
    local short = SHORT[c.id] or error("no short citation form for key: " .. c.id)
    local loc = pandoc.utils.stringify(c.suffix or {}):gsub("^%s*,%s*", "")
    local pre = pandoc.utils.stringify(c.prefix or {})
    local txt = (pre ~= "" and (pre .. " ") or "") .. short .. (loc ~= "" and (", " .. loc) or "")
    table.insert(parts, txt)
  end
  local md = table.concat(parts, "; ") .. "."
  local blocks = pandoc.read(md, "markdown").blocks
  return pandoc.Note(blocks)
end
