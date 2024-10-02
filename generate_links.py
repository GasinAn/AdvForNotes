from pathlib import Path

PROJECT_URL = "https://github.com/GasinAn/AdvForNotes/blob/main"
ADD_LINK_START_SYMBOL, ADD_LINK_END_SYMBOL = "<!--", "-->"

md_paths = [path for path in Path(".").rglob("*.md")]

for md_path in md_paths:
    with open(md_path, "r") as f:
        md_contents = f.readlines()

    for i in range(len(md_contents)):
        md_content = md_contents[i][:-1]

        if (md_content.startswith(ADD_LINK_START_SYMBOL) and
            md_content.endswith(ADD_LINK_END_SYMBOL)):
            link_dir = (md_content
                        .replace(ADD_LINK_START_SYMBOL, "")
                        .replace(ADD_LINK_END_SYMBOL, ""))
            link_title = link_dir.replace("_", " ")
            link_md = f"{link_dir}/{link_dir}.md"
            link_url = (f"{PROJECT_URL}/{md_path.parent}/{link_md}"
                        .replace("/./", "/")) # md_path.parent may be ".".
            link = f"[{link_title}]({link_url})\n"
            md_contents[i+1] = link

    with open(md_path, "w") as f:
        f.write("".join(md_contents))
