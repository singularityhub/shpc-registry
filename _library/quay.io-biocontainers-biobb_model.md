---
layout: container
name:  "quay.io/biocontainers/biobb_model"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_model/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_model/container.yaml"
updated_at: "2022-10-27 00:34:58.332511"
latest: "3.8.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_model"
aliases:
 - "check_structure"
 - "checking_log"
 - "fix_amides"
 - "fix_backbone"
 - "fix_chirality"
 - "fix_side_chain"
 - "mutate"
versions:
 - "3.8.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_model"
config: {"url": "https://biocontainers.pro/tools/biobb_model", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_model", "latest": {"3.8.0--pyhdfd78af_0": "sha256:b166cdac4abfb4d5e77ff3b74c587a381a42f8d798ab90a2abb5a99b99fa9ea1"}, "tags": {"3.8.0--pyhdfd78af_0": "sha256:b166cdac4abfb4d5e77ff3b74c587a381a42f8d798ab90a2abb5a99b99fa9ea1"}, "docker": "quay.io/biocontainers/biobb_model", "aliases": {"check_structure": "/usr/local/bin/check_structure", "checking_log": "/usr/local/bin/checking_log", "fix_amides": "/usr/local/bin/fix_amides", "fix_backbone": "/usr/local/bin/fix_backbone", "fix_chirality": "/usr/local/bin/fix_chirality", "fix_side_chain": "/usr/local/bin/fix_side_chain", "mutate": "/usr/local/bin/mutate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_model.
shpc-registry automated BioContainers addition for biobb_model
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_model
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_model:3.8.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_model/3.8.0--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_model/3.8.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_model-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_model-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_model-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_model-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_model-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_model-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check_structure

```bash
$ singularity exec <container> /usr/local/bin/check_structure
$ podman run --it --rm --entrypoint /usr/local/bin/check_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checking_log

```bash
$ singularity exec <container> /usr/local/bin/checking_log
$ podman run --it --rm --entrypoint /usr/local/bin/checking_log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checking_log   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_amides

```bash
$ singularity exec <container> /usr/local/bin/fix_amides
$ podman run --it --rm --entrypoint /usr/local/bin/fix_amides   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_amides   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_backbone

```bash
$ singularity exec <container> /usr/local/bin/fix_backbone
$ podman run --it --rm --entrypoint /usr/local/bin/fix_backbone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_backbone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_chirality

```bash
$ singularity exec <container> /usr/local/bin/fix_chirality
$ podman run --it --rm --entrypoint /usr/local/bin/fix_chirality   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_chirality   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_side_chain

```bash
$ singularity exec <container> /usr/local/bin/fix_side_chain
$ podman run --it --rm --entrypoint /usr/local/bin/fix_side_chain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_side_chain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutate

```bash
$ singularity exec <container> /usr/local/bin/mutate
$ podman run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
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