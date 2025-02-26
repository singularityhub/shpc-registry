---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowbeads"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowbeads/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowbeads/container.yaml"
updated_at: "2025-02-26 03:27:36.614255"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowbeads"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowbeads"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowbeads", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowbeads", "latest": {"1.44.0--r44hdfd78af_0": "sha256:bd4d53d136d64547409baa9a087afbd3a52e6b7d2163241541046fcdae8dc6df"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:ad6df167921a77f7deaa707414edfd5502657093a538331ff013106abfd2c3ca", "1.36.0--r42hdfd78af_0": "sha256:b308e705d2ab4fd835d0d3bdd29faa474ba42634b895379cd792887812752e2c", "1.38.0--r43hdfd78af_0": "sha256:0181b28e3bd874804cca0746ffbaed02fda8f4058103f3bfc35879299c68e5e3", "1.40.0--r43hdfd78af_0": "sha256:aa926743185d5096b15f0ddc8303054644c1af6aa1c506483dcd1731aecfd645", "1.44.0--r44hdfd78af_0": "sha256:bd4d53d136d64547409baa9a087afbd3a52e6b7d2163241541046fcdae8dc6df"}, "docker": "quay.io/biocontainers/bioconductor-flowbeads"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowbeads.
shpc-registry automated BioContainers addition for bioconductor-flowbeads
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowbeads
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowbeads:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowbeads/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowbeads/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowbeads-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowbeads-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowbeads-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowbeads-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowbeads-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowbeads-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowbeads

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