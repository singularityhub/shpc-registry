---
layout: container
name:  "quay.io/biocontainers/gmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gmap/container.yaml"
updated_at: "2025-07-22 00:57:55.274753"
latest: "2025.04.19--pl5321hb1d24b7_0"
container_url: "https://biocontainers.pro/tools/gmap"

versions:
 - "2020.06.01--pl526h2f06484_1"
 - "2024.02.22--h9d449c0_0"
 - "2023.12.01--h9d449c0_0"
 - "2023.10.10--h9d449c0_1"
 - "2023.07.20--h9d449c0_1"
 - "2023.06.01--h9d449c0_0"
 - "2024.03.15--h9d449c0_1"
 - "2024.05.07--pl5321h9d449c0_0"
 - "2024.03.15--pl5321h9d449c0_2"
 - "2024.05.20--pl5321h9d449c0_0"
 - "2024.08.14--pl5321h9d449c0_0"
 - "2024.09.18--pl5321h9d449c0_0"
 - "2024.10.20--pl5321h9d449c0_0"
 - "2024.11.20--pl5321h9d449c0_0"
 - "2024.11.20--pl5321hb1d24b7_1"
 - "2024.11.20--pl5321hb1d24b7_2"
 - "2025.04.19--pl5321hb1d24b7_0"
 - "2024.11.20--pl5321hb1d24b7_3"
description: "shpc-registry automated BioContainers addition for gmap"
config: {"url": "https://biocontainers.pro/tools/gmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gmap", "latest": {"2025.04.19--pl5321hb1d24b7_0": "sha256:4bb2cd36057c398b16452e7495721c7cd9f4d6c9ea990b88f95cf67a68cf9718"}, "tags": {"2020.06.01--pl526h2f06484_1": "sha256:a4cf2182c8b982aa4e8214fcbc12b5acd88c8da1e751d005a9bb14e2c13358a8", "2024.02.22--h9d449c0_0": "sha256:c148f79cb0dff711da4469e4d4ff38a17d6b8524f5fbb0a93f0cedd79f99b817", "2023.12.01--h9d449c0_0": "sha256:d026f4c247543cd25e63fb1df9f8ad59335ce0e20d15b6ca11d29e9dac6a6233", "2023.10.10--h9d449c0_1": "sha256:66b71ed998dfad8bde8a114f9023a4039b939c9ed63a15acd24f96978dc5b3df", "2023.07.20--h9d449c0_1": "sha256:23fc44e13e8fed1277a1a2014006ffd1242107f219ee439c0ef48c160be56edd", "2023.06.01--h9d449c0_0": "sha256:4d4ad32be25de4e55920d392cfd8c60f0fcba3d672ba707eece257ee85710adb", "2024.03.15--h9d449c0_1": "sha256:d235feb81700a150677cf5cd5289beaf3eb3e5827408bdb0186bb6869704f279", "2024.05.07--pl5321h9d449c0_0": "sha256:8f4b12a6f1e8d77e4c9e1dd2777157ac7ac2aecdb161feebe6f2561f778544a5", "2024.03.15--pl5321h9d449c0_2": "sha256:0a9734310933bd0361a72c41a1b34a55ea043dc91e9cad586212f7e32b816d38", "2024.05.20--pl5321h9d449c0_0": "sha256:8fb3d7ec91e57595b1f5bcfc27a2a79f602271429483c0f5112cff454ca10149", "2024.08.14--pl5321h9d449c0_0": "sha256:18efffee9f4c656d576773d82e3f5eae329293f20f5ca9a57adc57166567878d", "2024.09.18--pl5321h9d449c0_0": "sha256:9e99a5d060fd7edcaab64c86d38e993dc5340fc6599982e6037df058add2af21", "2024.10.20--pl5321h9d449c0_0": "sha256:d6745b4879638cd3e26a5d6ff131b7b2e37143342dfe7977ce83b3eb41b3e519", "2024.11.20--pl5321h9d449c0_0": "sha256:a994432e80a2dbbae300c14a2db2b033777cbe7e70be8312d37e81cb392f4a7d", "2024.11.20--pl5321hb1d24b7_1": "sha256:2aadbf392a86326b37565ac578a4d900e556febfad805aa253c3397d57e5922a", "2024.11.20--pl5321hb1d24b7_2": "sha256:d4eb00861322f9078374b8ee8c235b9d92d9c3916be977311ba77486e0bb4007", "2025.04.19--pl5321hb1d24b7_0": "sha256:4bb2cd36057c398b16452e7495721c7cd9f4d6c9ea990b88f95cf67a68cf9718", "2024.11.20--pl5321hb1d24b7_3": "sha256:656036199eb1006d9e23b49bc31576129707c9360025766677caaa71d7f28123"}, "docker": "quay.io/biocontainers/gmap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gmap.
shpc-registry automated BioContainers addition for gmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gmap:2025.04.19--pl5321hb1d24b7_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gmap/2025.04.19--pl5321hb1d24b7_0
$ module help quay.io/biocontainers/gmap/2025.04.19--pl5321hb1d24b7_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gmap

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