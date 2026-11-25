import {spawnSync} from 'node:child_process';
const result=spawnSync(process.env.PYTHON||'python',['scripts/build.py'],{cwd:new URL('..',import.meta.url),stdio:'inherit'});
process.exit(result.status??1);
