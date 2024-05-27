---
layout: container
name:  "quay.io/biocontainers/bioconductor-cogps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cogps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cogps/container.yaml"
updated_at: "2024-05-27 03:41:10.412920"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cogps"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cogps"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cogps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cogps", "latest": {"1.46.0--r43hdfd78af_0": "sha256:f8028ef47f22fb7ed229e0c77b7124a81002054e9fe2d198b18d5868b5ff0dea"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:26b887ecc8fff72c0035efdb6e21e1757886e701783c330d9b4428cb9b3bcea7", "1.42.0--r42hdfd78af_0": "sha256:79f0205d5c54dbcd548ca6299a14980d03f416f05f81bdbc0e5f309582dad5b2", "1.44.0--r43hdfd78af_0": "sha256:d38eb220bad5984b4a67e0975a187b8a784fad614fb01b56d259725541c752b1", "1.46.0--r43hdfd78af_0": "sha256:f8028ef47f22fb7ed229e0c77b7124a81002054e9fe2d198b18d5868b5ff0dea"}, "docker": "quay.io/biocontainers/bioconductor-cogps"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cogps.
shpc-registry automated BioContainers addition for bioconductor-cogps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cogps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cogps:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cogps/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cogps/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cogps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cogps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cogps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cogps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cogps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cogps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cogps

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