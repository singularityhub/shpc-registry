---
layout: container
name:  "quay.io/biocontainers/easypqp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/easypqp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/easypqp/container.yaml"
updated_at: "2026-01-26 04:58:17.474054"
latest: "0.1.54--pyhdfd78af_0"
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
 - "0.1.47--pyhdfd78af_0"
 - "0.1.49--pyhdfd78af_0"
 - "0.1.50--pyhdfd78af_0"
 - "0.1.50--pyhdfd78af_1"
 - "0.1.51--pyhdfd78af_0"
 - "0.1.52--pyhdfd78af_0"
 - "0.1.53--pyhdfd78af_0"
 - "0.1.54--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for easypqp"
config: {"url": "https://biocontainers.pro/tools/easypqp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for easypqp", "latest": {"0.1.54--pyhdfd78af_0": "sha256:9464e8c29c6713d1c2013f15d969cc01bd30a76e2f8e7927bb6e26758dd792d7"}, "tags": {"0.1.9--py_0": "sha256:efcf721422625e00ac551c33a533fec687a0cd4e52bb93aa5648f255b5b26b23", "0.1.32--pyhdfd78af_0": "sha256:6ad75c09290082fa1f1704960847d1364c67ac52fa37c913ad2880bd11aedbdf", "0.1.35--pyhdfd78af_0": "sha256:17040c83be70d3f6ff53e18671d42f14410063c207c94ea0432a01e69e21b3e4", "0.1.36--pyhdfd78af_0": "sha256:f5bf6ab13125c8945b3df98eea118e866f33d6d5aee956fe7c0a6b089c9f83fc", "0.1.37--pyhdfd78af_0": "sha256:5591dc48bafb8dd0a683727443a5136e9c3c4572fb385c3b98d36cac13f54ac9", "0.1.40--pyhdfd78af_0": "sha256:7462ed117e74317edf81241532a56cc7e17279aa8def9ad5a87f3e4861e1d778", "0.1.41--pyhdfd78af_0": "sha256:fa51748d28ad60199293ebc8a97c88198808c9c93a291d8bcf42758ee17a30fd", "0.1.42--pyhdfd78af_0": "sha256:289961fff91065205eb0771083f5dafdbbd958452592d50079a2eef5fbd7c27d", "0.1.44--pyhdfd78af_0": "sha256:5edabc0bc5f9f3c8e9a4fb6ef9a757e9d41bb56837e0115e7f8a2e8b7e4c888a", "0.1.47--pyhdfd78af_0": "sha256:05d590b16e65a9dbacc9665e56020e6dde80fe046bb0668c0ff65fc4802ff297", "0.1.49--pyhdfd78af_0": "sha256:94e6ab7ab473dff7014140a31fb46bd281697b79bfd3e3b3b8898822a50dc0a2", "0.1.50--pyhdfd78af_0": "sha256:82ec6181308514b01ce4618fd410732de501d1620738007944a7c119b409bdfa", "0.1.50--pyhdfd78af_1": "sha256:b7c6650a9cafb4b2aba797c6d34be35073e646a49b6689bc8cf4b45e4f68549f", "0.1.51--pyhdfd78af_0": "sha256:47b94be2ac5d0968e72635c124bab8539d8c7e006c65a4ace7c9188b1c83c9c4", "0.1.52--pyhdfd78af_0": "sha256:2c088fce3af0702d8515170cfebe942f1af51ccc4e173f16c935bb44a5eb99db", "0.1.53--pyhdfd78af_0": "sha256:a379fe03927a3c4d8d74cfa09664c354c161c4db9869962970036fbe72d2676e", "0.1.54--pyhdfd78af_0": "sha256:9464e8c29c6713d1c2013f15d969cc01bd30a76e2f8e7927bb6e26758dd792d7"}, "docker": "quay.io/biocontainers/easypqp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/easypqp.
shpc-registry automated BioContainers addition for easypqp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/easypqp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/easypqp:0.1.54--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/easypqp/0.1.54--pyhdfd78af_0
$ module help quay.io/biocontainers/easypqp/0.1.54--pyhdfd78af_0
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