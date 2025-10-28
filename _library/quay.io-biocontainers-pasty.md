---
layout: container
name:  "quay.io/biocontainers/pasty"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pasty/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pasty/container.yaml"
updated_at: "2025-10-28 03:12:50.369313"
latest: "2.2.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pasty"
aliases:
 - "executor"
 - "pasty"
 - "rich-click"
 - "cmark"
 - "coloredlogs"
 - "humanfriendly"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
versions:
 - "1.0.0--hdfd78af_0"
 - "1.0.2--hdfd78af_0"
 - "1.0.3--hdfd78af_0"
 - "2.0.0--hdfd78af_0"
 - "2.2.1--hdfd78af_0"
 - "2.1.0--hdfd78af_0"
 - "2.0.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for pasty"
config: {"url": "https://biocontainers.pro/tools/pasty", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pasty", "latest": {"2.2.1--hdfd78af_0": "sha256:2176d371c9061e8ad52bbac90b3eca5f1b79888d9fc59a6f7df845ba92c1c841"}, "tags": {"1.0.0--hdfd78af_0": "sha256:8bfb41cd6285c342bc63462a7395af3f8426cf919dd13fa76e27bdddfd876926", "1.0.2--hdfd78af_0": "sha256:ee6395b9e95f881a37c0087417af97aece538fe13b884afc5397a679f19cf827", "1.0.3--hdfd78af_0": "sha256:55fb1629cc3a2939fca1024033d4ae7ed430939c09ee9727f5fb475b851939cb", "2.0.0--hdfd78af_0": "sha256:d086f01fcdf0f4657e1ea001edce1a83c9e4b47e343122374909ee3fb0d21ef6", "2.2.1--hdfd78af_0": "sha256:2176d371c9061e8ad52bbac90b3eca5f1b79888d9fc59a6f7df845ba92c1c841", "2.1.0--hdfd78af_0": "sha256:0856fd104ac9bacd9c6652049b64b821f8c7df3bc9f8909829ce2eaa57f9ecb1", "2.0.2--hdfd78af_1": "sha256:619cfdd4b251bfb93f58022901eb8c54b583b3d808be188e48146716319e7be0"}, "docker": "quay.io/biocontainers/pasty", "aliases": {"executor": "/usr/local/bin/executor", "pasty": "/usr/local/bin/pasty", "rich-click": "/usr/local/bin/rich-click", "cmark": "/usr/local/bin/cmark", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pasty.
shpc-registry automated BioContainers addition for pasty
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pasty
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pasty:2.2.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pasty/2.2.1--hdfd78af_0
$ module help quay.io/biocontainers/pasty/2.2.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pasty-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pasty-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pasty-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pasty-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pasty-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pasty-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### executor

```bash
$ singularity exec <container> /usr/local/bin/executor
$ podman run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasty

```bash
$ singularity exec <container> /usr/local/bin/pasty
$ podman run --it --rm --entrypoint /usr/local/bin/pasty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)