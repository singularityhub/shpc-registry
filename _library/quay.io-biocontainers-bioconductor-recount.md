---
layout: container
name:  "quay.io/biocontainers/bioconductor-recount"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-recount/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-recount/container.yaml"
updated_at: "2025-02-02 03:25:56.644174"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-recount"

versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.1--r40hdfd78af_0"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-recount"
config: {"url": "https://biocontainers.pro/tools/bioconductor-recount", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-recount", "latest": {"1.32.0--r44hdfd78af_0": "sha256:26ed5743b26eacd190915af24d0bd746185c18dac803d5adca822ee7936f2518"}, "tags": {"1.8.1--r351_0": "sha256:f31e4db586506310f8cc08e798890758ce397af2811c85749d04b9c690b3f625", "1.24.0--r42hdfd78af_0": "sha256:029a0f5a334118eaa727c642eb41b080d4ff88f23139a6605e9672b3a6b033f3", "1.20.0--r41hdfd78af_0": "sha256:4029834487f7fc7035d79c933a410b33a93585c629ea358068ec05b1d1a06f5f", "1.18.0--r41hdfd78af_0": "sha256:e6fbc982d8ce8ce73e0c34947f293d6569ffbcd80a5e8d3e173e521824285477", "1.16.1--r40hdfd78af_0": "sha256:ef712e7b0f30f86eee1c9149e8f959a586f6332d93f87262705ed0f81228e123", "1.14.0--r40_0": "sha256:5ca000875a5eaaf87ce395d51242efaea7026eb0758ee6a96c1e9ae45be4ee55", "1.26.0--r43hdfd78af_0": "sha256:c6ff45525a999dcab09b2e7507c433fedc2eb2788b874585a468fe241d2ded6e", "1.28.0--r43hdfd78af_0": "sha256:27ea1d2170343ec944e14dfa83a331b25d4d93bddd8a2a37ddee932a9d13036d", "1.32.0--r44hdfd78af_0": "sha256:26ed5743b26eacd190915af24d0bd746185c18dac803d5adca822ee7936f2518"}, "docker": "quay.io/biocontainers/bioconductor-recount"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-recount.
shpc-registry automated BioContainers addition for bioconductor-recount
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-recount
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-recount:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-recount/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-recount/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-recount-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-recount-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-recount-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-recount-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-recount-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-recount-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-recount

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