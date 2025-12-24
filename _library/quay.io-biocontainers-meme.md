---
layout: container
name:  "quay.io/biocontainers/meme"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/meme/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/meme/container.yaml"
updated_at: "2025-12-24 04:17:56.285641"
latest: "5.5.9--pl5321h1ca524f_0"
container_url: "https://biocontainers.pro/tools/meme"

versions:
 - "5.1.1--py36pl526ha39971a_2"
 - "5.5.5--pl5321hda358d9_0"
 - "5.4.1--py310pl5321hb021246_2"
 - "5.3.0--py37pl5262h2b62359_2"
 - "5.1.1--py38pl526hc1f1133_3"
 - "5.5.5--pl5321h62c8895_1"
 - "5.5.6--pl5321h4242488_0"
 - "5.5.7--pl5321hca22f42_0"
 - "5.5.7--pl5321h1ca524f_1"
 - "5.5.7--pl5321h1ca524f_2"
 - "5.5.7--pl5321h1ca524f_3"
 - "5.5.8--pl5321h1ca524f_0"
 - "5.5.9--pl5321h1ca524f_0"
description: "shpc-registry automated BioContainers addition for meme"
config: {"url": "https://biocontainers.pro/tools/meme", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for meme", "latest": {"5.5.9--pl5321h1ca524f_0": "sha256:b75247dfaab1707dcdff6075a331b122affe9c5eaa1f82e5ed4a701fc75486ca"}, "tags": {"5.1.1--py36pl526ha39971a_2": "sha256:e3e0b38a966ff909ceb573fa9072399c27eed5266f2a02ca9875a6f04461b1a4", "5.5.5--pl5321hda358d9_0": "sha256:5a7a2c7ba931e310f132c7d94aa7505fa0ad717d159011d49881c72fd1ec3c2a", "5.4.1--py310pl5321hb021246_2": "sha256:a6183efb91c299ca6c5ae59a7ac202c18b7d1c6ee4ac1c4d7fd497fd43665f4b", "5.3.0--py37pl5262h2b62359_2": "sha256:9a3aca0b5701137e40e0bf8345a608a0611e31d1f87dd2d2db059d1be8690424", "5.1.1--py38pl526hc1f1133_3": "sha256:fe700133e60700fef230f1dc661f079b968f9179b193b4602bfba185dd31c4b0", "5.5.5--pl5321h62c8895_1": "sha256:040406a4d954310d51e1b580006fe5468664ad48d8b632c445e8b45751edf4f0", "5.5.6--pl5321h4242488_0": "sha256:71dbdb1d33046dc8f53966541998c529d1920cd22d6ec9e8579b3bdd07cccbcf", "5.5.7--pl5321hca22f42_0": "sha256:9791ce63bef20af1626ec7312c9141c723aab9d0bc9ef80695790671c0367be6", "5.5.7--pl5321h1ca524f_1": "sha256:127de6607fe71cb1bb384143b72ad69667b20f8fd68a87e28aaefad5262d6db3", "5.5.7--pl5321h1ca524f_2": "sha256:52686bd48a084622fa68a8b647b7feecd5d9fd5ef81260df1be964a5d6580d9d", "5.5.7--pl5321h1ca524f_3": "sha256:2a67bf6502b23f2a32ab21b550a2f8475c58e7d0840ee50d8d22327972580cc8", "5.5.8--pl5321h1ca524f_0": "sha256:cf25bbc72dbf4eec9e663dec12ab2314e42f4d05c6d2fa6738c6292a3f6470e2", "5.5.9--pl5321h1ca524f_0": "sha256:b75247dfaab1707dcdff6075a331b122affe9c5eaa1f82e5ed4a701fc75486ca"}, "docker": "quay.io/biocontainers/meme"}
---

This module is a singularity container wrapper for quay.io/biocontainers/meme.
shpc-registry automated BioContainers addition for meme
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/meme
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/meme:5.5.9--pl5321h1ca524f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/meme/5.5.9--pl5321h1ca524f_0
$ module help quay.io/biocontainers/meme/5.5.9--pl5321h1ca524f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### meme-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### meme-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### meme-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### meme-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### meme-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### meme-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### meme

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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