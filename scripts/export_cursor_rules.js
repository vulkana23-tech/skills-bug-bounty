const fs = require('fs');
const path = require('path');

const srcDir = path.join(__dirname, '..', 'skills');
const dstWorkspace = path.join(__dirname, '..', '.cursor', 'rules');
const userHome = process.env.USERPROFILE || process.env.HOME;
const dstGlobal = path.join(userHome, '.cursor', 'rules');

fs.mkdirSync(dstWorkspace, { recursive: true });
fs.mkdirSync(dstGlobal, { recursive: true });

const skillFolders = fs.readdirSync(srcDir, { withFileTypes: true })
  .filter(dirent => dirent.isDirectory())
  .map(dirent => dirent.name);

let count = 0;
for (const folder of skillFolders) {
  const skillFile = path.join(srcDir, folder, 'SKILL.md');
  if (fs.existsSync(skillFile)) {
    const content = fs.readFileSync(skillFile, 'utf-8');
    const mdcFilename = `${folder}.mdc`;
    
    // Add Cursor MDC frontmatter if not present
    let mdcContent = content;
    if (!content.startsWith('---')) {
      mdcContent = `---\ndescription: ${folder} skill methodology\nglobs: *\n---\n\n` + content;
    }
    
    fs.writeFileSync(path.join(dstWorkspace, mdcFilename), mdcContent, 'utf-8');
    fs.writeFileSync(path.join(dstGlobal, mdcFilename), mdcContent, 'utf-8');
    count++;
  }
}

console.log(`[+] Successfully converted ${count} skills to Cursor .mdc rules in both workspace (.cursor/rules/) and global (~/.cursor/rules/)!`);
