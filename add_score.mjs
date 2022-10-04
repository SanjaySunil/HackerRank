#!/usr/bin/env node
import fs from "fs";
import inquirer from "inquirer";

let data = fs.readFileSync("scores/problem_solving.json");

let json = JSON.parse(data);

const get = (key, path) => {
  return new Promise((resolve, reject) => {
    let tempfile = [];
    Object.keys(path).forEach((x) => tempfile.push(x));
    inquirer
      .prompt([
        {
          type: "list",
          name: key,
          message: `${key}: `,
          choices: tempfile,
        },
      ])
      .then((answers) => {
        resolve(answers[key]);
      })
      .catch((e) => {
        reject(e);
      });
  });
};

const input = (key) => {
  return new Promise((resolve, reject) => {
    inquirer
      .prompt([
        {
          type: "input",
          name: key,
          message: `${key}: `,
        },
      ])
      .then((answers) => {
        resolve(answers[key]);
      })
      .catch((e) => {
        reject(e);
      });
  });
};

get("domain", json).then((domain) => {
  get("sub_domain", json[domain]).then((sub_domain) => {
    get("difficulty", json[domain][sub_domain]).then((difficulty) => {
      input("problem name").then((problem) => {
        input("score").then((score) => {
          input("out of").then((out_of) => {
            json[domain][sub_domain][difficulty][problem] = [
              Number(score),
              Number(out_of),
            ];
            fs.writeFileSync(
              "scores/problem_solving.json",
              JSON.stringify(json, null, 2)
            );
            console.log("Finished.");
          });
        });
      });
    });
  });
});
