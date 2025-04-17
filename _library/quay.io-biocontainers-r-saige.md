---
layout: container
name:  "quay.io/biocontainers/r-saige"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-saige/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-saige/container.yaml"
updated_at: "2025-04-17 03:05:29.851726"
latest: "1.3.1--r44h38d2662_2"
container_url: "https://biocontainers.pro/tools/r-saige"
aliases:
 - "bgenix"
 - "cat-bgen"
 - "createSparseGRM.R"
 - "edit-bgen"
 - "extractNglmm.R"
 - "sav"
 - "step1_fitNULLGLMM.R"
 - "step2_SPAtests.R"
versions:
 - "0.45.0--r41h723e9af_4"
 - "1.3.1--r43h3710e3a_0"
 - "1.2.0--r43h3710e3a_0"
 - "1.1.9--r43h3710e3a_3"
 - "0.45.0--r42h723e9af_5"
 - "1.3.1--r43h774bd07_1"
 - "1.3.1--r44h38d2662_2"
description: "shpc-registry automated BioContainers addition for r-saige"
config: {"url": "https://biocontainers.pro/tools/r-saige", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-saige", "latest": {"1.3.1--r44h38d2662_2": "sha256:5aed0453e5cbd22ab75d82e6d9a1deb350579c44932163c1fecc71b9235d2318"}, "tags": {"0.45.0--r41h723e9af_4": "sha256:066611caaba72656958979750db871e1d4b81fcc0d44ba3bcffb513ac1847117", "1.3.1--r43h3710e3a_0": "sha256:82d70aa1e6378163cda6d9763b5d07197bf28b061829465a481a527c93993870", "1.2.0--r43h3710e3a_0": "sha256:d03a88069d2ed0be316b4c0686c70400400016c872b8b9620bdef986c5c3eb59", "1.1.9--r43h3710e3a_3": "sha256:e05dc3b783f726045ff1ac096e387abe407db5364140ba8703b7731bfaeda43d", "0.45.0--r42h723e9af_5": "sha256:0e1d81b3f49d4286b2c4edd9c68a24f1b3c1da2a0821d271a83380a407067eaa", "1.3.1--r43h774bd07_1": "sha256:e179f91c924ca7ca9b440284ee4e838d9a9d8b2c417698191d7374f4c8da9512", "1.3.1--r44h38d2662_2": "sha256:5aed0453e5cbd22ab75d82e6d9a1deb350579c44932163c1fecc71b9235d2318"}, "docker": "quay.io/biocontainers/r-saige", "aliases": {"bgenix": "/usr/local/bin/bgenix", "cat-bgen": "/usr/local/bin/cat-bgen", "createSparseGRM.R": "/usr/local/bin/createSparseGRM.R", "edit-bgen": "/usr/local/bin/edit-bgen", "extractNglmm.R": "/usr/local/bin/extractNglmm.R", "sav": "/usr/local/bin/sav", "step1_fitNULLGLMM.R": "/usr/local/bin/step1_fitNULLGLMM.R", "step2_SPAtests.R": "/usr/local/bin/step2_SPAtests.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-saige.
shpc-registry automated BioContainers addition for r-saige
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-saige
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-saige:1.3.1--r44h38d2662_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-saige/1.3.1--r44h38d2662_2
$ module help quay.io/biocontainers/r-saige/1.3.1--r44h38d2662_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-saige-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-saige-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-saige-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-saige-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-saige-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-saige-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bgenix

```bash
$ singularity exec <container> /usr/local/bin/bgenix
$ podman run --it --rm --entrypoint /usr/local/bin/bgenix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgenix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cat-bgen

```bash
$ singularity exec <container> /usr/local/bin/cat-bgen
$ podman run --it --rm --entrypoint /usr/local/bin/cat-bgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat-bgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createSparseGRM.R

```bash
$ singularity exec <container> /usr/local/bin/createSparseGRM.R
$ podman run --it --rm --entrypoint /usr/local/bin/createSparseGRM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createSparseGRM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edit-bgen

```bash
$ singularity exec <container> /usr/local/bin/edit-bgen
$ podman run --it --rm --entrypoint /usr/local/bin/edit-bgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edit-bgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractNglmm.R

```bash
$ singularity exec <container> /usr/local/bin/extractNglmm.R
$ podman run --it --rm --entrypoint /usr/local/bin/extractNglmm.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractNglmm.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sav

```bash
$ singularity exec <container> /usr/local/bin/sav
$ podman run --it --rm --entrypoint /usr/local/bin/sav   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sav   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### step1_fitNULLGLMM.R

```bash
$ singularity exec <container> /usr/local/bin/step1_fitNULLGLMM.R
$ podman run --it --rm --entrypoint /usr/local/bin/step1_fitNULLGLMM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/step1_fitNULLGLMM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### step2_SPAtests.R

```bash
$ singularity exec <container> /usr/local/bin/step2_SPAtests.R
$ podman run --it --rm --entrypoint /usr/local/bin/step2_SPAtests.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/step2_SPAtests.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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