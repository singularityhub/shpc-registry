---
layout: container
name:  "quay.io/biocontainers/cytoscape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cytoscape/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cytoscape/container.yaml"
updated_at: "2024-09-08 03:12:26.760486"
latest: "3.10.2--he65b2d3_0"
container_url: "https://biocontainers.pro/tools/cytoscape"
aliases:
 - "Cytoscape"
 - "cytoscape.sh"
 - "gen_vmoptions.sh"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
versions:
 - "3.9.1--hadc2ddb_0"
 - "3.9.1--he65b2d3_1"
 - "3.10.1--he65b2d3_0"
 - "3.10.2--he65b2d3_0"
description: "shpc-registry automated BioContainers addition for cytoscape"
config: {"url": "https://biocontainers.pro/tools/cytoscape", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cytoscape", "latest": {"3.10.2--he65b2d3_0": "sha256:f39c384ec38a4dca4868560dd073881412c5b5f6e8e922dd88f8668303635cf9"}, "tags": {"3.9.1--hadc2ddb_0": "sha256:080341a76cb6855437cd126b260c5d9443dbc1bdc7f453793b21fd344212b312", "3.9.1--he65b2d3_1": "sha256:ace1e1888db6aa701ffb6bd352ed7c441107acaf04dfe0aa30808b63713850eb", "3.10.1--he65b2d3_0": "sha256:b862e314c907a2956c82f5b6b35481ca8ae8194529533b3d1008d044b4a3422d", "3.10.2--he65b2d3_0": "sha256:f39c384ec38a4dca4868560dd073881412c5b5f6e8e922dd88f8668303635cf9"}, "docker": "quay.io/biocontainers/cytoscape", "aliases": {"Cytoscape": "/usr/local/bin/Cytoscape", "cytoscape.sh": "/usr/local/bin/cytoscape.sh", "gen_vmoptions.sh": "/usr/local/bin/gen_vmoptions.sh", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cytoscape.
shpc-registry automated BioContainers addition for cytoscape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cytoscape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cytoscape:3.10.2--he65b2d3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cytoscape/3.10.2--he65b2d3_0
$ module help quay.io/biocontainers/cytoscape/3.10.2--he65b2d3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cytoscape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cytoscape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cytoscape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cytoscape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cytoscape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cytoscape-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Cytoscape

```bash
$ singularity exec <container> /usr/local/bin/Cytoscape
$ podman run --it --rm --entrypoint /usr/local/bin/Cytoscape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Cytoscape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cytoscape.sh

```bash
$ singularity exec <container> /usr/local/bin/cytoscape.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cytoscape.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cytoscape.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gen_vmoptions.sh

```bash
$ singularity exec <container> /usr/local/bin/gen_vmoptions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gen_vmoptions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gen_vmoptions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
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