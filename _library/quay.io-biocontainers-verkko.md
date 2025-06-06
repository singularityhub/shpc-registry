---
layout: container
name:  "quay.io/biocontainers/verkko"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/verkko/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/verkko/container.yaml"
updated_at: "2025-06-06 12:52:12.991943"
latest: "2.2.1--h45dadce_0"
container_url: "https://biocontainers.pro/tools/verkko"

versions:
 - "1.1--h64afbab_0"
 - "1.2--h64afbab_0"
 - "1.1--h64afbab_1"
 - "1.3.1--h64afbab_0"
 - "1.4--h48217b1_0"
 - "1.4.1--h48217b1_0"
 - "2.1--h45dadce_0"
 - "2.0--h45dadce_0"
 - "2.2--h45dadce_0"
 - "2.2.1--h45dadce_0"
description: "shpc-registry automated BioContainers addition for verkko"
config: {"url": "https://biocontainers.pro/tools/verkko", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for verkko", "latest": {"2.2.1--h45dadce_0": "sha256:1d17089c1a4faeb415944ffefaca7d2d780e2732f1a60a337b20a026b9168a6f"}, "tags": {"1.1--h64afbab_0": "sha256:7f5e46ea6b03f3d1873c4a06b681f24a9db1bda10a03d4b0e59f0a4d881d6d4a", "1.2--h64afbab_0": "sha256:d4f8db736d1df768b5afc2b5d8e4f29634356f6f51f0a6eb8c411a4835fbfb4f", "1.1--h64afbab_1": "sha256:d88c307bac8a0dfed25ec704fe2a48ccb9fd306ff7f82e35797d9411765eada4", "1.3.1--h64afbab_0": "sha256:8926929ff7a981038908e25a3712c26044084b059c71b2578a6883d0043d55a8", "1.4--h48217b1_0": "sha256:84b01d7fa81b2b21989115eac69a3e8f8130ff53087aa82ac21abc34ba15277f", "1.4.1--h48217b1_0": "sha256:31294e26380b8bbc774f9d070f62d8e325195e7d91f6d20e6a69aa7a55928560", "2.1--h45dadce_0": "sha256:456ac5d6b08916d2f347783617d699b6418ae1c026e44873f8b54eda0ca4f141", "2.0--h45dadce_0": "sha256:433f9ae6888c4ffa0eeab8697a01adb156e4f97326c9e331f06e4eb5837655a6", "2.2--h45dadce_0": "sha256:65f05cd1552ee11a4dc4d7805fc7108f962f27595934fa4848566be41e0bc6bc", "2.2.1--h45dadce_0": "sha256:1d17089c1a4faeb415944ffefaca7d2d780e2732f1a60a337b20a026b9168a6f"}, "docker": "quay.io/biocontainers/verkko"}
---

This module is a singularity container wrapper for quay.io/biocontainers/verkko.
shpc-registry automated BioContainers addition for verkko
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/verkko
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/verkko:2.2.1--h45dadce_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/verkko/2.2.1--h45dadce_0
$ module help quay.io/biocontainers/verkko/2.2.1--h45dadce_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### verkko-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### verkko-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### verkko-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### verkko-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### verkko-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### verkko-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### verkko

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