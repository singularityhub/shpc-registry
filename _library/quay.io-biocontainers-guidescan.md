---
layout: container
name:  "quay.io/biocontainers/guidescan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/guidescan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/guidescan/container.yaml"
updated_at: "2024-04-04 04:19:02.734024"
latest: "2.2.0--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/guidescan"
aliases:
 - "guidescan_bamdata"
 - "guidescan_cutting_efficiency_processer"
 - "guidescan_cutting_specificity_processer"
 - "guidescan_guidequery"
 - "guidescan_processer"
 - "rename"
 - "enhancer.py"
 - "explode.py"
 - "gifmaker.py"
 - "painter.py"
 - "player.py"
 - "thresholder.py"
 - "viewer.py"
 - "pilconvert.py"
 - "pildriver.py"
versions:
 - "1.2--0"
 - "2.0.0--h9f5acd7_0"
 - "2.1.2--h9f5acd7_0"
 - "2.1.4--h9f5acd7_0"
 - "2.1.4--h4ac6f70_2"
 - "2.1.5--h4ac6f70_0"
 - "2.1.7--h4ac6f70_0"
 - "2.2.0--h4ac6f70_0"
 - "2.1.8--h4ac6f70_0"
description: "shpc-registry automated BioContainers addition for guidescan"
config: {"url": "https://biocontainers.pro/tools/guidescan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for guidescan", "latest": {"2.2.0--h4ac6f70_0": "sha256:53103ee140f870c58c37a7b3da95e09e1fb90914950408971cdc2a70e55920b3"}, "tags": {"1.2--0": "sha256:129aa8ba50df3be5a28a4411a12a4a39c2e0804017545e83713b8dc8882620d4", "2.0.0--h9f5acd7_0": "sha256:e8c450cb505f5984359b74dd93b90eaa5ad9e2c46a38c74400ed07252a80bfa1", "2.1.2--h9f5acd7_0": "sha256:ab7cdf7366209a861450044054b1a49099edbee75acb03d67dfc25c281ab6c89", "2.1.4--h9f5acd7_0": "sha256:6fb0f001ada3fa184b3016c7697f613de25a76f3fbb8afec5cb7977b09184b24", "2.1.4--h4ac6f70_2": "sha256:d9e51a79860893a7330d62bb0305af3487f2600a357bff26f29203061f4e3095", "2.1.5--h4ac6f70_0": "sha256:a60568e6fa8b8be5d8380a5afe38048de0efd6769f922121bd006233be6225ee", "2.1.7--h4ac6f70_0": "sha256:54deafe7b22829536e1a49e8a2417c397e9c07fc6eed887ecc150f09a7994107", "2.2.0--h4ac6f70_0": "sha256:53103ee140f870c58c37a7b3da95e09e1fb90914950408971cdc2a70e55920b3", "2.1.8--h4ac6f70_0": "sha256:ca41005b95a8a892b2a5f6154c0d018db30634e2a36376e52d9cfad961dbf054"}, "docker": "quay.io/biocontainers/guidescan", "aliases": {"guidescan_bamdata": "/usr/local/bin/guidescan_bamdata", "guidescan_cutting_efficiency_processer": "/usr/local/bin/guidescan_cutting_efficiency_processer", "guidescan_cutting_specificity_processer": "/usr/local/bin/guidescan_cutting_specificity_processer", "guidescan_guidequery": "/usr/local/bin/guidescan_guidequery", "guidescan_processer": "/usr/local/bin/guidescan_processer", "rename": "/usr/local/bin/rename", "enhancer.py": "/usr/local/bin/enhancer.py", "explode.py": "/usr/local/bin/explode.py", "gifmaker.py": "/usr/local/bin/gifmaker.py", "painter.py": "/usr/local/bin/painter.py", "player.py": "/usr/local/bin/player.py", "thresholder.py": "/usr/local/bin/thresholder.py", "viewer.py": "/usr/local/bin/viewer.py", "pilconvert.py": "/usr/local/bin/pilconvert.py", "pildriver.py": "/usr/local/bin/pildriver.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/guidescan.
shpc-registry automated BioContainers addition for guidescan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/guidescan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/guidescan:2.2.0--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/guidescan/2.2.0--h4ac6f70_0
$ module help quay.io/biocontainers/guidescan/2.2.0--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### guidescan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### guidescan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### guidescan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### guidescan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### guidescan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### guidescan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### guidescan_bamdata

```bash
$ singularity exec <container> /usr/local/bin/guidescan_bamdata
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_bamdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_bamdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidescan_cutting_efficiency_processer

```bash
$ singularity exec <container> /usr/local/bin/guidescan_cutting_efficiency_processer
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_cutting_efficiency_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_cutting_efficiency_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidescan_cutting_specificity_processer

```bash
$ singularity exec <container> /usr/local/bin/guidescan_cutting_specificity_processer
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_cutting_specificity_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_cutting_specificity_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidescan_guidequery

```bash
$ singularity exec <container> /usr/local/bin/guidescan_guidequery
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_guidequery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_guidequery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidescan_processer

```bash
$ singularity exec <container> /usr/local/bin/guidescan_processer
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename

```bash
$ singularity exec <container> /usr/local/bin/rename
$ podman run --it --rm --entrypoint /usr/local/bin/rename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enhancer.py

```bash
$ singularity exec <container> /usr/local/bin/enhancer.py
$ podman run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### explode.py

```bash
$ singularity exec <container> /usr/local/bin/explode.py
$ podman run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifmaker.py

```bash
$ singularity exec <container> /usr/local/bin/gifmaker.py
$ podman run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### painter.py

```bash
$ singularity exec <container> /usr/local/bin/painter.py
$ podman run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### player.py

```bash
$ singularity exec <container> /usr/local/bin/player.py
$ podman run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thresholder.py

```bash
$ singularity exec <container> /usr/local/bin/thresholder.py
$ podman run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viewer.py

```bash
$ singularity exec <container> /usr/local/bin/viewer.py
$ podman run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilconvert.py

```bash
$ singularity exec <container> /usr/local/bin/pilconvert.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pildriver.py

```bash
$ singularity exec <container> /usr/local/bin/pildriver.py
$ podman run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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