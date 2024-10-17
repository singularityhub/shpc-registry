---
layout: container
name:  "quay.io/biocontainers/bioconductor-netprior"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-netprior/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-netprior/container.yaml"
updated_at: "2024-10-17 18:24:08.907423"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-netprior"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-netprior"
config: {"url": "https://biocontainers.pro/tools/bioconductor-netprior", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-netprior", "latest": {"1.28.0--r43hdfd78af_0": "sha256:ba904dcf7186c8b623c124f1473fbb6a136c3683d353b9fe2b6846414ff6136d"}, "tags": {"1.8.1--r351_0": "sha256:c9586f11ffa9e232f4abe8984b455a647aebcec1254ef0568ad1e763e7bc471b", "1.24.0--r42hdfd78af_0": "sha256:2952dcd049fd31eb8a86095f520b268ffe716b50656780fdfb0e7ffb99feed9f", "1.20.0--r41hdfd78af_0": "sha256:790a3115fdef12bbda17f02485fd8f065b5f6af64775b0d21a6b817f165e14da", "1.18.0--r41hdfd78af_0": "sha256:968ac85cd9cdf252b690b8338255e97967d4832ae984bcd5f48cc26ced9d8ce0", "1.16.0--r40hdfd78af_1": "sha256:ff7972d477e3106b1c2a2c85e9e5f2e5fb8556a80b844076dfe4416b31cdb6b5", "1.14.0--r40_0": "sha256:44cfea74ec1c0e67edee871f1dfe7832d34e5ce9ae8b4a73df767edb8ce1ff94", "1.26.0--r43hdfd78af_0": "sha256:114d9764150555e6dae440cae89f181d29d8a7171e18b49b72fa8e7807335b5f", "1.28.0--r43hdfd78af_0": "sha256:ba904dcf7186c8b623c124f1473fbb6a136c3683d353b9fe2b6846414ff6136d"}, "docker": "quay.io/biocontainers/bioconductor-netprior", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-netprior.
shpc-registry automated BioContainers addition for bioconductor-netprior
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-netprior
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-netprior:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-netprior/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-netprior/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-netprior-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netprior-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netprior-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-netprior-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-netprior-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-netprior-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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