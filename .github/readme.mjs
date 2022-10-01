import { createMarkdownArrayTableSync } from "parse-markdown-table";
import README from "readme-components";
import fs from "fs";

let template = new README();
const markdown = fs.readFileSync("readme_components/table.md", {
  encoding: "utf-8",
});

const table = createMarkdownArrayTableSync(markdown);
let total = 0;
let solved = 0
for (const row of table.rows) {
  const num = Number(row[4]);
  if (Number.isInteger(num)) {
    total = total + num;
    solved++;
  }
}

template.use_component("./readme_components/header.md");
template.use_component("./readme_components/shields.md", { solved, score: total });
template.use_component("./readme_components/table.md");

template.make_readme();
