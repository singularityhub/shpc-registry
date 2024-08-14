---
layout: container
name:  "quay.io/biocontainers/taxonkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/taxonkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/taxonkit/container.yaml"
updated_at: "2024-08-14 02:46:09.175598"
latest: "0.17.0--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/taxonkit"
aliases:
 - "taxonkit"
versions:
 - "0.9.0--h9ee0642_0"
 - "0.13.0--h9ee0642_0"
 - "0.12.0--h9ee0642_0"
 - "0.11.1--h9ee0642_0"
 - "0.10.1--h9ee0642_0"
 - "0.14.0--h9ee0642_0"
 - "0.14.1--h9ee0642_0"
 - "0.14.2--h9ee0642_0"
 - "0.15.0--h9ee0642_0"
 - "0.15.1--h9ee0642_0"
 - "0.16.0--h9ee0642_0"
 - "0.16.0--h9ee0642_1"
 - "0.17.0--h9ee0642_0"
 - "0.17.0--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for taxonkit"
config: {"url": "https://biocontainers.pro/tools/taxonkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for taxonkit", "latest": {"0.17.0--h9ee0642_1": "sha256:66f3e549f4abc92c1e9d683a0c0342667ff261122c753125726e9afb07c016c0"}, "tags": {"0.9.0--h9ee0642_0": "sha256:af690fd2053972ea7572d57d3df433a5dc04150eb3cdd0a41b3fa417c67cea7d", "0.13.0--h9ee0642_0": "sha256:fe310da17a905b9c9087b845496731f44a84b8467464770899ccd4fa41f12202", "0.12.0--h9ee0642_0": "sha256:b0b396fe321720093c2ac42a8a4d722c087eb090ef0d595b24acdf50b1e6f303", "0.11.1--h9ee0642_0": "sha256:3e81ea86d1918b477c4c301c4b44c1e17386b67df8c22165bf4c227ac36f0361", "0.10.1--h9ee0642_0": "sha256:36a782dd788fc806e910b70ef34e28bf5bb44d49fcaf661ed0011d1fe6bbf7c5", "0.14.0--h9ee0642_0": "sha256:256042c0844ddf792d9a2fe9aac4859bf3efee7c9c8834613f6773bcdf05166c", "0.14.1--h9ee0642_0": "sha256:a2cd57387109854daf8d7766f2e2a12701f630f2d28640c3cf2da02faaac5765", "0.14.2--h9ee0642_0": "sha256:03f7df94d1c2be8f3821b2b278f937a9e0e8668382049b1555073fc92e0e32f8", "0.15.0--h9ee0642_0": "sha256:5b853805d76580dc8e51563909713af9a12cea75aa55c9813a92bb37e39d39e8", "0.15.1--h9ee0642_0": "sha256:111506b0470bbe77717e33776a59aba15c6dc125f8d3d3e8add35a5a333f622f", "0.16.0--h9ee0642_0": "sha256:2d5e5868c5958dd9ba236828a5dab9a84cb04034dd41a2f1feec2144ad24bc12", "0.16.0--h9ee0642_1": "sha256:c094243c863854c3e6e7c2bad5ae9439b3047655e3b4de597c927cefae4645c0", "0.17.0--h9ee0642_0": "sha256:e9df6ee5e77e1b813415b24ba95bc1d151d19d786eb5dcb8e519607db32b6579", "0.17.0--h9ee0642_1": "sha256:66f3e549f4abc92c1e9d683a0c0342667ff261122c753125726e9afb07c016c0"}, "docker": "quay.io/biocontainers/taxonkit", "aliases": {"taxonkit": "/usr/local/bin/taxonkit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/taxonkit.
shpc-registry automated BioContainers addition for taxonkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/taxonkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/taxonkit:0.17.0--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/taxonkit/0.17.0--h9ee0642_1
$ module help quay.io/biocontainers/taxonkit/0.17.0--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### taxonkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### taxonkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### taxonkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### taxonkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### taxonkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### taxonkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### taxonkit

```bash
$ singularity exec <container> /usr/local/bin/taxonkit
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
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