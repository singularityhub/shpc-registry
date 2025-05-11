---
layout: container
name:  "quay.io/biocontainers/delly"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/delly/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/delly/container.yaml"
updated_at: "2025-05-11 04:01:05.302264"
latest: "1.3.3--h4d20210_1"
container_url: "https://biocontainers.pro/tools/delly"
aliases:
 - "delly"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.1.5--ha41ced6_1"
 - "1.1.6--ha41ced6_0"
 - "1.1.6--h2af1cb8_1"
 - "1.1.6--h6b1aa3f_2"
 - "1.1.7--h6b1aa3f_0"
 - "1.1.8--hb7e2ac5_0"
 - "1.2.6--hb7e2ac5_0"
 - "1.2.6--hb7e2ac5_1"
 - "1.2.6--hdcf5f25_3"
 - "1.2.6--hdcf5f25_4"
 - "1.2.9--hf9970c3_0"
 - "1.3.1--hf9970c3_0"
 - "1.3.1--h4d20210_1"
 - "1.3.3--h4d20210_0"
 - "1.3.3--h4d20210_1"
description: "shpc-registry automated BioContainers addition for delly"
config: {"url": "https://biocontainers.pro/tools/delly", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for delly", "latest": {"1.3.3--h4d20210_1": "sha256:67ea846395b2beb42a5034a1c9bfa96f3fd480b045e9efa0dd504901a0c71cda"}, "tags": {"1.1.5--ha41ced6_1": "sha256:d6bf4e579f3b588d59e744cfbac51752b9a901af8dae06a22be65f436539dcd7", "1.1.6--ha41ced6_0": "sha256:1483554d377d5b30d98d2aa040a3eb33d6710b0caffe5e1002a047f36c21f452", "1.1.6--h2af1cb8_1": "sha256:1374d649c50930088fb7a4fd867e349f18036266e4d7c6800081b57b9a6fbbfc", "1.1.6--h6b1aa3f_2": "sha256:dce012f682fcb19cf07ae2e933d52666329f74dc50ce5aaac9e59c15ed9eea66", "1.1.7--h6b1aa3f_0": "sha256:04904f5e666e3e8d5fa44e1829bd66f1d4adaa68bffa3295c3ba98a7e26ccd61", "1.1.8--hb7e2ac5_0": "sha256:441c0d09e6a4f2d8af849001573a0501ea54c8824ddd7f6b8cacf2b804876a97", "1.2.6--hb7e2ac5_0": "sha256:5c00ed597d8f5a278bc4f190711f81c47cee70ef92211c1b6140f331bee5965d", "1.2.6--hb7e2ac5_1": "sha256:928d90f18f1f9a2d27ceef0b8550562cbf4980b62ceb10673f8952c03c497668", "1.2.6--hdcf5f25_3": "sha256:d1a4d5ed0c5074a5401d7462e29a2ea70b191b0d88f824cfb30158f3e274c63a", "1.2.6--hdcf5f25_4": "sha256:663c12e14adc4c44ff6b8f3b298b6cce108c87aebf8fbdf331fbfb839f96053a", "1.2.9--hf9970c3_0": "sha256:b0aa33d205c647848b1a53b88433a0fdb35c934829ea7365b73d81c4917f451c", "1.3.1--hf9970c3_0": "sha256:32c9310fd13170e8a55caf1f2230488ac2ca27902af5f3c9e0ef850e30a51e51", "1.3.1--h4d20210_1": "sha256:e43568efa9113d7199b4d6467746e7fe334603b603e9c456fabb4154261f7f40", "1.3.3--h4d20210_0": "sha256:06430f146b5087781f14fc62465ee3e5694d7d6fd3b821a5ec3dab7145086025", "1.3.3--h4d20210_1": "sha256:67ea846395b2beb42a5034a1c9bfa96f3fd480b045e9efa0dd504901a0c71cda"}, "docker": "quay.io/biocontainers/delly", "aliases": {"delly": "/usr/local/bin/delly", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/delly.
shpc-registry automated BioContainers addition for delly
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/delly
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/delly:1.3.3--h4d20210_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/delly/1.3.3--h4d20210_1
$ module help quay.io/biocontainers/delly/1.3.3--h4d20210_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### delly-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### delly-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### delly-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### delly-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### delly-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### delly-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### delly

```bash
$ singularity exec <container> /usr/local/bin/delly
$ podman run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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