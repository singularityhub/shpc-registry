---
layout: container
name:  "quay.io/biocontainers/bioconductor-saturn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-saturn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-saturn/container.yaml"
updated_at: "2024-06-09 02:45:25.227252"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-saturn"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-saturn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-saturn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-saturn", "latest": {"1.10.0--r43hdfd78af_0": "sha256:75c1fe96b97e3720f7ee6df80014c89bc24fd1c087c959828ddf68f1390a8b5a"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:ff4efb4a8ae186a15af6df52a28d203859f6ba829cc796214b359a250ebc06bb", "1.6.0--r42hdfd78af_0": "sha256:280c51bba7dfb57a67490d448ef51080269b7ed88eddb849d19b1129c5b9dd2a", "1.8.0--r43hdfd78af_0": "sha256:ce3e3389c23894ddb7b64425121866e10e389b313ae22d334d6bad636c081041", "1.10.0--r43hdfd78af_0": "sha256:75c1fe96b97e3720f7ee6df80014c89bc24fd1c087c959828ddf68f1390a8b5a"}, "docker": "quay.io/biocontainers/bioconductor-saturn"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-saturn.
shpc-registry automated BioContainers addition for bioconductor-saturn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-saturn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-saturn:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-saturn/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-saturn/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-saturn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-saturn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-saturn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-saturn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-saturn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-saturn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-saturn

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