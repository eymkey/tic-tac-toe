##GIT Convention

###Code Of Conduct
1. Do not use commands you do not understand or are not used to
2. Always as for help before doing strange things

###Allowed

####Actions
|command |arguments |description |comment |
|-----------|---------------|-----------------------------------|-------------------------------|
| add | [files...] | adds file to staged area | . for all files |
| commit | | creates commit from staged area |
| checkout | branch | switches to another branch |
| fetch | | fetches branches and refs |
| merge | branch | updates HEAD to the latest commit | only fastforward merges |

####Display Information
|command |arguments |description |comment |
|-----------|-------------------|---------------------------------------|-----------|
| status | | shows working tree status |
| diff | [commit1 commit2] | shows difference between two commits |
| log | --all --graph | shows commit history | 
| branch | -a | shows all local and remote branches | 
| remote | -v | shows all remote connections |

###Review Required
|command |arguments |description |comment |
|-----------|-----------------------|---------------------------------------|-------------------------------|
| checkout | -b branch | creates a new branch |
| merge | branch | merges two branches to a single commit | all non fastforward merges |
| push | [-u] remote branch | pushes local commits to the server |

##Workflow

###Starting Your Work

|command |description |
|-------|----------|
| git fetch |
| git log --all --graph | check if everything is ok |
| git merge | only fastforward merges, look at the commit history |

###Commits
Try to create as little as possible commits. Only commit if a logical task ist completed. Seperate your commit message into header - blank line - body. Use the imperativ in the header (add, update, change, etc.) Always check your branch before commiting.

```
Header

First line of the body.
Second line of the body.
```

###Three Way Merging
1. checkout to master
2. look at the commit history if everything is as expected
3. git merge [to-be-marged-branch]
4. resolve merge conflicts
5. git commit

###Pushing
Pushing must always be approved by a second person. Do not push unless you have a fully understanding of all effects.