import README from "readme-components";
import fs from "fs";
import { markdownTable } from "markdown-table";
import titleCase from './utils/titleCase.mjs';
import problem_solving from "../scores/problem_solving.json" assert { type: "json" };

let solved = 0;
let score = 0;
let template = new README();

Object.keys(problem_solving).forEach(function (domain) {
  Object.keys(problem_solving[domain]).forEach(function (sub_domain) {
    let sub_domain_table = [
      ["Difficulty", "Problem", "Solution", "Score Obtained", "Max Score"],
    ];
    Object.keys(problem_solving[domain][sub_domain]).forEach(function (
      difficulty
    ) {
      Object.keys(problem_solving[domain][sub_domain][difficulty]).forEach(
        function (problem) {
          console.log(problem);
          sub_domain_table.push([
            titleCase(difficulty),
            `[${titleCase(problem.replaceAll("_", " "))}](https://www.hackerrank.com/challenges/${problem.replaceAll("_", "-")}/problem)`,
            titleCase(
              `[${problem}.py](/problem_solving/${domain}/${sub_domain}/${difficulty}/${problem}.py)`
            ),
            Object.values(
              problem_solving[domain][sub_domain][difficulty][problem]
            )[0],
            Object.values(
              problem_solving[domain][sub_domain][difficulty][problem]
            )[1],
          ]);
          solved++;
          score =
            score +
            Object.values(
              problem_solving[domain][sub_domain][difficulty][problem]
            )[0];
        }
      );
    });
    let data = markdownTable(sub_domain_table);
    console.log(sub_domain_table);
    fs.writeFileSync(`readme_components/algorithms/${sub_domain}.md`, data);
  });
});

let markdown_tables =
  "This repository contains my solutions to the HackerRank `Problem Solving` course. The topic is split into two domains, [algorithms](https://www.hackerrank.com/domains/algorithms) and [data structures](https://www.hackerrank.com/domains/data-structures).\n\n";
Object.keys(problem_solving).forEach(function (domain) {
  markdown_tables =
    markdown_tables + `## ${titleCase(domain.replace("_", " "))}` + "\n";
  Object.keys(problem_solving[domain]).forEach(function (sub_domain) {
    let markdown = fs.readFileSync(
      `./readme_components/${domain}/${sub_domain}.md`,
      {
        encoding: "utf-8",
      }
    );
    const file_header = `### ${titleCase(sub_domain.replace(".md", ""))}`;
    markdown_tables = markdown_tables + file_header + "\n" + markdown + "\n\n";
  });
});

fs.writeFileSync(`readme_components/problem_solving.md`, markdown_tables);

template.use_component("./readme_components/header.md");
template.use_component("./readme_components/shields.md", {
  solved,
  score,
});
template.use_component("./readme_components/problem_solving.md");

template.make_readme();
