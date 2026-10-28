// Voice a text with the SuperClonica speech API (Node.js 18+, no packages).
// SUPERCLONICA_KEY=sc_... node speak.mjs "Hello from Node!"
import { writeFile } from "node:fs/promises";

const text = process.argv.slice(2).join(" ") || "Hello! This voice comes from a free API.";
const answer = await fetch("https://superclonica.com/api/v1/speech", {
  method: "POST",
  headers: { Authorization: `Bearer ${process.env.SUPERCLONICA_KEY}`, "Content-Type": "application/json" },
  body: JSON.stringify({ text, voice: "M2", language: "en", format: "mp3" }),
});
if (!answer.ok) throw new Error(`${answer.status}: ${await answer.text()}`);
await writeFile("speech.mp3", Buffer.from(await answer.arrayBuffer()));
console.log("saved speech.mp3");
