---
layout: container
name:  "quay.io/biocontainers/megagta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/megagta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/megagta/container.yaml"
updated_at: "2023-07-03 03:43:28.376816"
latest: "0.1_alpha--0"
container_url: "https://biocontainers.pro/tools/megagta"
aliases:
 - "hmmc2"
 - "hmmerfm-exactmatch"
 - "megagta"
 - "megagta.py"
 - "post_proc.sh"
 - "prepare_gene_ref.sh"
 - "xander_customized_hmmer_version_for_prepare_gene.sh"
 - "easy_install-2.7"
 - "alimask"
 - "hmmconvert"
 - "hmmemit"
 - "hmmfetch"
 - "hmmlogo"
 - "hmmpgmd"
 - "hmmpress"
 - "hmmscan"
 - "hmmsearch"
versions:
 - "0.1_alpha--0"
description: "shpc-registry automated BioContainers addition for megagta"
config: {"url": "https://biocontainers.pro/tools/megagta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for megagta", "latest": {"0.1_alpha--0": "sha256:f3f14565d01c4c836f2da609a418f35c1e2f14c9fbcf88e7c9e14a54dbdd639b"}, "tags": {"0.1_alpha--0": "sha256:f3f14565d01c4c836f2da609a418f35c1e2f14c9fbcf88e7c9e14a54dbdd639b"}, "docker": "quay.io/biocontainers/megagta", "aliases": {"hmmc2": "/usr/local/bin/hmmc2", "hmmerfm-exactmatch": "/usr/local/bin/hmmerfm-exactmatch", "megagta": "/usr/local/bin/megagta", "megagta.py": "/usr/local/bin/megagta.py", "post_proc.sh": "/usr/local/bin/post_proc.sh", "prepare_gene_ref.sh": "/usr/local/bin/prepare_gene_ref.sh", "xander_customized_hmmer_version_for_prepare_gene.sh": "/usr/local/bin/xander_customized_hmmer_version_for_prepare_gene.sh", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "alimask": "/usr/local/bin/alimask", "hmmconvert": "/usr/local/bin/hmmconvert", "hmmemit": "/usr/local/bin/hmmemit", "hmmfetch": "/usr/local/bin/hmmfetch", "hmmlogo": "/usr/local/bin/hmmlogo", "hmmpgmd": "/usr/local/bin/hmmpgmd", "hmmpress": "/usr/local/bin/hmmpress", "hmmscan": "/usr/local/bin/hmmscan", "hmmsearch": "/usr/local/bin/hmmsearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/megagta.
shpc-registry automated BioContainers addition for megagta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/megagta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/megagta:0.1_alpha--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/megagta/0.1_alpha--0
$ module help quay.io/biocontainers/megagta/0.1_alpha--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### megagta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### megagta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### megagta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### megagta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### megagta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### megagta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hmmc2

```bash
$ singularity exec <container> /usr/local/bin/hmmc2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerfm-exactmatch

```bash
$ singularity exec <container> /usr/local/bin/hmmerfm-exactmatch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megagta

```bash
$ singularity exec <container> /usr/local/bin/megagta
$ podman run --it --rm --entrypoint /usr/local/bin/megagta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megagta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megagta.py

```bash
$ singularity exec <container> /usr/local/bin/megagta.py
$ podman run --it --rm --entrypoint /usr/local/bin/megagta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megagta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### post_proc.sh

```bash
$ singularity exec <container> /usr/local/bin/post_proc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/post_proc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/post_proc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare_gene_ref.sh

```bash
$ singularity exec <container> /usr/local/bin/prepare_gene_ref.sh
$ podman run --it --rm --entrypoint /usr/local/bin/prepare_gene_ref.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare_gene_ref.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xander_customized_hmmer_version_for_prepare_gene.sh

```bash
$ singularity exec <container> /usr/local/bin/xander_customized_hmmer_version_for_prepare_gene.sh
$ podman run --it --rm --entrypoint /usr/local/bin/xander_customized_hmmer_version_for_prepare_gene.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xander_customized_hmmer_version_for_prepare_gene.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmconvert

```bash
$ singularity exec <container> /usr/local/bin/hmmconvert
$ podman run --it --rm --entrypoint /usr/local/bin/hmmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmemit

```bash
$ singularity exec <container> /usr/local/bin/hmmemit
$ podman run --it --rm --entrypoint /usr/local/bin/hmmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmfetch

```bash
$ singularity exec <container> /usr/local/bin/hmmfetch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmlogo

```bash
$ singularity exec <container> /usr/local/bin/hmmlogo
$ podman run --it --rm --entrypoint /usr/local/bin/hmmlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpress

```bash
$ singularity exec <container> /usr/local/bin/hmmpress
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmscan

```bash
$ singularity exec <container> /usr/local/bin/hmmscan
$ podman run --it --rm --entrypoint /usr/local/bin/hmmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmsearch

```bash
$ singularity exec <container> /usr/local/bin/hmmsearch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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