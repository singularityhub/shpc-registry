---
layout: container
name:  "quay.io/biocontainers/bioconductor-drimseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drimseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drimseq/container.yaml"
updated_at: "2024-01-02 02:42:35.564284"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-drimseq"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-drimseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drimseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drimseq", "latest": {"1.30.0--r43hdfd78af_0": "sha256:ee3e0c9ce8d4b220034c4c8c41e1bfdd43c818092fc083e42d30393b2347dd4a"}, "tags": {"1.8.0--r351_0": "sha256:ae5067b1a546a3191c2e0ea8410113b480cd758be4e11dc780ad9514d21778bb", "1.26.0--r42hdfd78af_0": "sha256:467c435649f1473f803c44ca9985f622016ebd47ea53ad661861f5a940febed7", "1.22.0--r41hdfd78af_0": "sha256:691497d1325afda97d21ef986dd9a1e9b48582cf648e255990ca75eaa5d2e9dc", "1.20.0--r41hdfd78af_0": "sha256:eb5606f3a41e4470f80f75057f159ba5a11049d2f200791ba0139bd4e0c7df28", "1.18.0--r40hdfd78af_1": "sha256:5f9969ee6a89ef41bd2ebed97a30d12411a393da357ec8cdfe57d08cc0074f84", "1.16.0--r40_0": "sha256:0ae588a1537937e46fbb999f7efe3beefa858a71295a02faaf22c77df47ee889", "1.28.0--r43hdfd78af_0": "sha256:b92a74952b3d66a19fb6ea8751e2e6e1fdf11b7d5e78c428f61515d7e14dfcb6", "1.30.0--r43hdfd78af_0": "sha256:ee3e0c9ce8d4b220034c4c8c41e1bfdd43c818092fc083e42d30393b2347dd4a"}, "docker": "quay.io/biocontainers/bioconductor-drimseq", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drimseq.
shpc-registry automated BioContainers addition for bioconductor-drimseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drimseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drimseq:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drimseq/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-drimseq/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drimseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drimseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drimseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drimseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drimseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drimseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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