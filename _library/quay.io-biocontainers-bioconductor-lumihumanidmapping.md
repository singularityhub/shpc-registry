---
layout: container
name:  "quay.io/biocontainers/bioconductor-lumihumanidmapping"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lumihumanidmapping/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lumihumanidmapping/container.yaml"
updated_at: "2023-12-30 02:58:22.679367"
latest: "1.10.1--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-lumihumanidmapping"

versions:
 - "1.10.1--r41hdfd78af_9"
 - "1.10.1--r42hdfd78af_10"
 - "1.10.1--r43hdfd78af_11"
 - "1.10.1--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-lumihumanidmapping"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lumihumanidmapping", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lumihumanidmapping", "latest": {"1.10.1--r43hdfd78af_12": "sha256:e4ee1e92c3baf9085478e48914d036296daeab7f5a57b4822e0751cd3422cc65"}, "tags": {"1.10.1--r41hdfd78af_9": "sha256:fb190bbfd75333dc8d18614711639135d3fafc8c0727877163678dd6cf5a3bca", "1.10.1--r42hdfd78af_10": "sha256:74a153bfa2e6a206cbfbd9f917126c73b2e5bae2c090cc44603e86e4788c4fea", "1.10.1--r43hdfd78af_11": "sha256:742d964defc9a676bac93bfcf8a3a737bb8392b4d433ff328c14fd137acefaae", "1.10.1--r43hdfd78af_12": "sha256:e4ee1e92c3baf9085478e48914d036296daeab7f5a57b4822e0751cd3422cc65"}, "docker": "quay.io/biocontainers/bioconductor-lumihumanidmapping"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lumihumanidmapping.
shpc-registry automated BioContainers addition for bioconductor-lumihumanidmapping
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lumihumanidmapping
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lumihumanidmapping:1.10.1--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lumihumanidmapping/1.10.1--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-lumihumanidmapping/1.10.1--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lumihumanidmapping-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumihumanidmapping-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumihumanidmapping-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lumihumanidmapping-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lumihumanidmapping-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lumihumanidmapping-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lumihumanidmapping

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