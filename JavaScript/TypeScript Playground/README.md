For compiling .ts to .js...
Install 'typescript' with npm. Better to do so globally. Compile with tsc.
```
tsc foo.ts
```

If you'd like to set up a listener to automatically compile updated code...
```
tsc -w -p .
```

For running .ts on the fly without writing .js compiled code to disk...
Install 'ts-node' in the project or globally and run with that.
```
npx ts-node foo.ts
```
(if it's global you shouldn't need npx, just directly run ts-node)