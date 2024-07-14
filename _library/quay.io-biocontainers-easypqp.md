---
layout: container
name:  "quay.io/biocontainers/easypqp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/easypqp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/easypqp/container.yaml"
updated_at: "2024-07-14 03:04:12.491735"
latest: "0.1.44--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/easypqp"

versions:
 - "0.1.9--py_0"
 - "0.1.32--pyhdfd78af_0"
 - "0.1.35--pyhdfd78af_0"
 - "0.1.36--pyhdfd78af_0"
 - "0.1.37--pyhdfd78af_0"
 - "0.1.40--pyhdfd78af_0"
 - "0.1.41--pyhdfd78af_0"
 - "0.1.42--pyhdfd78af_0"
 - "0.1.44--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for easypqp"
config: {"url": "https://biocontainers.pro/tools/easypqp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for easypqp", "latest": {"0.1.44--pyhdfd78af_0": "sha256:5edabc0bc5f9f3c8e9a4fb6ef9a757e9d41bb56837e0115e7f8a2e8b7e4c888a"}, "tags": {"0.1.9--py_0": "sha256:efcf721422625e00ac551c33a533fec687a0cd4e52bb93aa5648f255b5b26b23", "0.1.32--pyhdfd78af_0": "sha256:6ad75c09290082fa1f1704960847d1364c67ac52fa37c913ad2880bd11aedbdf", "0.1.35--pyhdfd78af_0": "sha256:17040c83be70d3f6ff53e18671d42f14410063c207c94ea0432a01e69e21b3e4", "0.1.36--pyhdfd78af_0": "sha256:f5bf6ab13125c8945b3df98eea118e866f33d6d5aee956fe7c0a6b089c9f83fc", "0.1.37--pyhdfd78af_0": "sha256:5591dc48bafb8dd0a683727443a5136e9c3c4572fb385c3b98d36cac13f54ac9", "0.1.40--pyhdfd78af_0": "sha256:7462ed117e74317edf81241532a56cc7e17279aa8def9ad5a87f3e4861e1d778", "0.1.41--pyhdfd78af_0": "sha256:fa51748d28ad60199293ebc8a97c88198808c9c93a291d8bcf42758ee17a30fd", "0.1.42--pyhdfd78af_0": "sha256:289961fff91065205eb0771083f5dafdbbd958452592d50079a2eef5fbd7c27d", "0.1.44--pyhdfd78af_0": "sha256:5edabc0bc5f9f3c8e9a4fb6ef9a757e9d41bb56837e0115e7f8a2e8b7e4c888a"}, "docker": "quay.io/biocontainers/easypqp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/easypqp.
shpc-registry automated BioContainers addition for easypqp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/easypqp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/easypqp:0.1.44--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/easypqp/0.1.44--pyhdfd78af_0
$ module help quay.io/biocontainers/easypqp/0.1.44--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### easypqp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### easypqp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### easypqp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### easypqp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### easypqp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### easypqp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### easypqp

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