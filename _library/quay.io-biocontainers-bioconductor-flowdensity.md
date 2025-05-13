---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowdensity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowdensity/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowdensity/container.yaml"
updated_at: "2025-05-13 03:45:16.573204"
latest: "1.40.0--r44h92aedd1_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowdensity"
aliases:
 - "uconv"
 - "tclsh8.5"
 - "wish8.5"
 - "ncursesw5-config"
versions:
 - "1.6.0--r3.3.2_0"
 - "1.32.0--r42hd91ffd7_0"
 - "1.28.0--r41hd91ffd7_0"
 - "1.26.0--r41hd91ffd7_0"
 - "1.24.0--r40hd91ffd7_1"
 - "1.22.0--r40hbc14f71_0"
 - "1.32.0--r42ha823636_1"
 - "1.34.0--r43hf0b54c8_0"
 - "1.36.1--r43hf0b54c8_0"
 - "1.36.1--r43h92aedd1_1"
 - "1.40.0--r44h92aedd1_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowdensity"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowdensity", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowdensity", "latest": {"1.40.0--r44h92aedd1_0": "sha256:148223628b0ce17efa8b9c13b3e2aa7f400083312df388fdaff4eb13651bd044"}, "tags": {"1.6.0--r3.3.2_0": "sha256:6fdba82cd036185d8119c5c2cef8fed07ba6f92e8c3bfa35e8074cced13fe02b", "1.32.0--r42hd91ffd7_0": "sha256:a44885f49467dbeec0d9e89efcf80343789376a4681c48a6df7a9f3fd1f41378", "1.28.0--r41hd91ffd7_0": "sha256:e64f16896d03c5acb65f2166fe8144490fb9cfb256d4afa2e2b3f92936a4a94e", "1.26.0--r41hd91ffd7_0": "sha256:fecd302e36feb7756cc24889823fcd3cdc9c428a9126d670d49776e1d97f69ed", "1.24.0--r40hd91ffd7_1": "sha256:1d0af0318cecd6db568a6ac6167588670c1d79c1c09237445eeb4669833ac380", "1.22.0--r40hbc14f71_0": "sha256:9c92d8703e269526f098bcb7183c9136ada67aca3d0a3864ce65e2810c942520", "1.32.0--r42ha823636_1": "sha256:807fbf1624e62c9e0575ba7ccb2f16508ba472722cbfe4441c4b8c884652e2f8", "1.34.0--r43hf0b54c8_0": "sha256:d863fd4c1b16edbe646642e88136a0fde813958da05b2c20081344cc7ca27b50", "1.36.1--r43hf0b54c8_0": "sha256:7f724f645eb0f8e2d2190b063c528d31e25eba992fd6e2fc6120bf3bcea53878", "1.36.1--r43h92aedd1_1": "sha256:7d81cbd7fd7e4115c08cb8a8a4933f3598305dbebbfd8ccbbae25dfcdfc970a3", "1.40.0--r44h92aedd1_0": "sha256:148223628b0ce17efa8b9c13b3e2aa7f400083312df388fdaff4eb13651bd044"}, "docker": "quay.io/biocontainers/bioconductor-flowdensity", "aliases": {"uconv": "/usr/local/bin/uconv", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowdensity.
shpc-registry automated BioContainers addition for bioconductor-flowdensity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowdensity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowdensity:1.40.0--r44h92aedd1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowdensity/1.40.0--r44h92aedd1_0
$ module help quay.io/biocontainers/bioconductor-flowdensity/1.40.0--r44h92aedd1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowdensity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowdensity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowdensity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowdensity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowdensity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowdensity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### uconv

```bash
$ singularity exec <container> /usr/local/bin/uconv
$ podman run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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