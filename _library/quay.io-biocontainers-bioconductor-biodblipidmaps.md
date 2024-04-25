---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodblipidmaps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodblipidmaps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodblipidmaps/container.yaml"
updated_at: "2024-04-25 03:16:08.988588"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biodblipidmaps"

versions:
 - "1.0.1--r41hdfd78af_0"
 - "1.3.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biodblipidmaps"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodblipidmaps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biodblipidmaps", "latest": {"1.8.0--r43hdfd78af_0": "sha256:a2ba4a0826761bb9d9b3fb6f03615438afdc8a46d5f88d2593cb2f1d564c3142"}, "tags": {"1.0.1--r41hdfd78af_0": "sha256:6513bc9a259df9cd54b8e28545d8183b39f4236ca2eee3718eb824903947c027", "1.3.0--r42hdfd78af_0": "sha256:2884580a992f29e03162a8022e2a71fc69bfa9c5253e1e3f833a856fda176cae", "1.6.0--r43hdfd78af_0": "sha256:bcc1e949e03ba194602d85b8ffa5398ed8aeaabbed81264be29901c2a2b0a24a", "1.8.0--r43hdfd78af_0": "sha256:a2ba4a0826761bb9d9b3fb6f03615438afdc8a46d5f88d2593cb2f1d564c3142"}, "docker": "quay.io/biocontainers/bioconductor-biodblipidmaps"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodblipidmaps.
shpc-registry automated BioContainers addition for bioconductor-biodblipidmaps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodblipidmaps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodblipidmaps:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodblipidmaps/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biodblipidmaps/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodblipidmaps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodblipidmaps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodblipidmaps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodblipidmaps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodblipidmaps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodblipidmaps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodblipidmaps

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