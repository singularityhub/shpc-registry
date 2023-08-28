---
layout: container
name:  "quay.io/biocontainers/bioconductor-trackviewer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-trackviewer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-trackviewer/container.yaml"
updated_at: "2023-08-28 03:53:25.012027"
latest: "1.36.2--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-trackviewer"

versions:
 - "1.30.0--r41hc247a5b_2"
 - "1.34.0--r42hc247a5b_0"
 - "1.34.0--r42hf17093f_1"
 - "1.36.2--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-trackviewer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-trackviewer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-trackviewer", "latest": {"1.36.2--r43hdfd78af_0": "sha256:c97c3fc250d43da18d827357429b853c54dc72c00d0edfa51f27b05b6bcfb041"}, "tags": {"1.30.0--r41hc247a5b_2": "sha256:03e7509cc2f6f2ac3e93d8317297c70058df55d0ccb9004a4a52b67cfb971b33", "1.34.0--r42hc247a5b_0": "sha256:3fe65bedd670cfff11f444724b9c21c68c021ff417b994ca98f222a495e6b696", "1.34.0--r42hf17093f_1": "sha256:0ea18c0f9803062563d8cb9514870d6a83d21f460ddb5ab94241027e8b826da5", "1.36.2--r43hdfd78af_0": "sha256:c97c3fc250d43da18d827357429b853c54dc72c00d0edfa51f27b05b6bcfb041"}, "docker": "quay.io/biocontainers/bioconductor-trackviewer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-trackviewer.
shpc-registry automated BioContainers addition for bioconductor-trackviewer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-trackviewer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-trackviewer:1.36.2--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-trackviewer/1.36.2--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-trackviewer/1.36.2--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-trackviewer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trackviewer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trackviewer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-trackviewer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-trackviewer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-trackviewer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-trackviewer

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