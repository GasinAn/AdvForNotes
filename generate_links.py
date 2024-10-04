from pathlib import Path

PROJECT_URL = "https://gasinan.github.io/AdvForNotes"
ADD_LINK_START_SYMBOL, ADD_LINK_END_SYMBOL = "<!--", "-->"

md_paths = [path for path in Path(".").rglob("*.md")]

for md_path in md_paths:
    with open(md_path, "r") as f:
        md_contents = f.readlines()

    for i in range(len(md_contents)):
        md_content = md_contents[i][:-1]

        if (md_content.startswith(ADD_LINK_START_SYMBOL) and
                md_content.endswith(ADD_LINK_END_SYMBOL)):
            link_name = (md_content
                         .replace(ADD_LINK_START_SYMBOL, "")
                         .replace(ADD_LINK_END_SYMBOL, ""))
            link_url = f"{PROJECT_URL}/{link_name}"
            link_title = link_name.replace("_", " ")
            link = f"[{link_title}]({link_url})\n"
            md_contents[i+1] = link

    with open(md_path, "w") as f:
        f.write("".join(md_contents))
