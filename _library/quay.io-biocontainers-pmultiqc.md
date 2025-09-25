---
layout: container
name:  "quay.io/biocontainers/pmultiqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pmultiqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pmultiqc/container.yaml"
updated_at: "2025-09-25 07:37:52.084640"
latest: "0.0.34--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pmultiqc"
aliases:
 - "parse_sdrf"
 - "multiqc"
 - "cmark"
 - "coloredlogs"
 - "humanfriendly"
 - "py.test"
 - "pytest"
 - "markdown_py"
 - "pygmentize"
 - "fonttools"
 - "pyftmerge"
versions:
 - "0.0.9--pyhdfd78af_0"
 - "0.0.17--pyhdfd78af_0"
 - "0.0.19--pyhdfd78af_0"
 - "0.0.20--pyhdfd78af_0"
 - "0.0.22--pyhdfd78af_0"
 - "0.0.23--pyhdfd78af_0"
 - "0.0.24--pyhdfd78af_0"
 - "0.0.25--pyhdfd78af_0"
 - "0.0.28--pyhdfd78af_0"
 - "0.0.33--pyhdfd78af_0"
 - "0.0.34--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pmultiqc"
config: {"url": "https://biocontainers.pro/tools/pmultiqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pmultiqc", "latest": {"0.0.34--pyhdfd78af_0": "sha256:b7e17954a4cfb00e700380a8923b0e52ca4e611dc93d53c9fcd5b335d771b18e"}, "tags": {"0.0.9--pyhdfd78af_0": "sha256:5a090cd18ad36694211f29ff1102d887b5404596ae3009e39a8b8cec8b4bde4a", "0.0.17--pyhdfd78af_0": "sha256:fa8f0d1dc290460d83e503ff1a5d18041f8ec3be7ef47ad7aacf25e71af12c1d", "0.0.19--pyhdfd78af_0": "sha256:ae406918645de12c0b7958c92114d350e23907e7b64d2b06c8743e2a173ce848", "0.0.20--pyhdfd78af_0": "sha256:5f64b69f92f826e225a2327b5ef57b0cf1e1f011190f7090ff93bf1b0eb12037", "0.0.22--pyhdfd78af_0": "sha256:c4db0310a85d9e93cefc2aea1b6e2d515689d043f60765fd38ffa88ca04ec22d", "0.0.23--pyhdfd78af_0": "sha256:90dbcd23de8836f131f468faee4fd02cb6cbca02484b42873188f54577eef5ff", "0.0.24--pyhdfd78af_0": "sha256:736ee913c42ef9ddc70760429f93de7070831fdb891f010182b6fe28f3d82663", "0.0.25--pyhdfd78af_0": "sha256:e13c0e2e3e99c1c5d68d57d45d32b51a944d19490cdddfb9b73869875ed745cf", "0.0.28--pyhdfd78af_0": "sha256:eeb58c414cee62fd6f34f486e62600fb3cb907785d9a12e7e33dd03e537852ac", "0.0.33--pyhdfd78af_0": "sha256:48c37797abf8651b8cdb52a57f94f001c4c54121950a254ce2b38ced05715039", "0.0.34--pyhdfd78af_0": "sha256:b7e17954a4cfb00e700380a8923b0e52ca4e611dc93d53c9fcd5b335d771b18e"}, "docker": "quay.io/biocontainers/pmultiqc", "aliases": {"parse_sdrf": "/usr/local/bin/parse_sdrf", "multiqc": "/usr/local/bin/multiqc", "cmark": "/usr/local/bin/cmark", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "markdown_py": "/usr/local/bin/markdown_py", "pygmentize": "/usr/local/bin/pygmentize", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pmultiqc.
shpc-registry automated BioContainers addition for pmultiqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pmultiqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pmultiqc:0.0.34--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pmultiqc/0.0.34--pyhdfd78af_0
$ module help quay.io/biocontainers/pmultiqc/0.0.34--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pmultiqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pmultiqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pmultiqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pmultiqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pmultiqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pmultiqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### parse_sdrf

```bash
$ singularity exec <container> /usr/local/bin/parse_sdrf
$ podman run --it --rm --entrypoint /usr/local/bin/parse_sdrf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse_sdrf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown_py

```bash
$ singularity exec <container> /usr/local/bin/markdown_py
$ podman run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
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