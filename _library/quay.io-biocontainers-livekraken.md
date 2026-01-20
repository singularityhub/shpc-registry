---
layout: container
name:  "quay.io/biocontainers/livekraken"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/livekraken/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/livekraken/container.yaml"
updated_at: "2026-01-20 03:58:11.509044"
latest: "1.0--pl5321h9948957_12"
container_url: "https://biocontainers.pro/tools/livekraken"
aliases:
 - "livekraken"
 - "livekraken-build"
 - "livekraken-filter"
 - "livekraken-mpa-report"
 - "livekraken-report"
 - "livekraken-translate"
 - "livekraken_sankey_diagram.py"
 - "jellyfish"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0--pl5321h2df963e_8"
 - "1.0--pl5321h376f1d3_9"
 - "1.0--pl5321h4ac6f70_10"
 - "1.0--pl5321h9948957_11"
 - "1.0--pl5321h9948957_12"
description: "shpc-registry automated BioContainers addition for livekraken"
config: {"url": "https://biocontainers.pro/tools/livekraken", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for livekraken", "latest": {"1.0--pl5321h9948957_12": "sha256:e5464cea6ac607612d0cfeeb0973b327642daea13e1c614946cd4253d225af38"}, "tags": {"1.0--pl5321h2df963e_8": "sha256:99864bf327e18d570639a46b10413f60c59719c72320dd16fe342dbf1b37008b", "1.0--pl5321h376f1d3_9": "sha256:29a1fbcecc0d59940c91f58a74831f73d27d7be0f07fca264f3c3069063136e0", "1.0--pl5321h4ac6f70_10": "sha256:89357f353388bc12fe884c808583f543c9734851399607066159db24c2f4af9e", "1.0--pl5321h9948957_11": "sha256:ed7ad74ee8d648846360d6f397957095121f6e0f285e3d53f2ae2670b3ddb8b0", "1.0--pl5321h9948957_12": "sha256:e5464cea6ac607612d0cfeeb0973b327642daea13e1c614946cd4253d225af38"}, "docker": "quay.io/biocontainers/livekraken", "aliases": {"livekraken": "/usr/local/bin/livekraken", "livekraken-build": "/usr/local/bin/livekraken-build", "livekraken-filter": "/usr/local/bin/livekraken-filter", "livekraken-mpa-report": "/usr/local/bin/livekraken-mpa-report", "livekraken-report": "/usr/local/bin/livekraken-report", "livekraken-translate": "/usr/local/bin/livekraken-translate", "livekraken_sankey_diagram.py": "/usr/local/bin/livekraken_sankey_diagram.py", "jellyfish": "/usr/local/bin/jellyfish", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/livekraken.
shpc-registry automated BioContainers addition for livekraken
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/livekraken
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/livekraken:1.0--pl5321h9948957_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/livekraken/1.0--pl5321h9948957_12
$ module help quay.io/biocontainers/livekraken/1.0--pl5321h9948957_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### livekraken-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### livekraken-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### livekraken-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### livekraken-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### livekraken-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### livekraken-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### livekraken

```bash
$ singularity exec <container> /usr/local/bin/livekraken
$ podman run --it --rm --entrypoint /usr/local/bin/livekraken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/livekraken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### livekraken-build

```bash
$ singularity exec <container> /usr/local/bin/livekraken-build
$ podman run --it --rm --entrypoint /usr/local/bin/livekraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/livekraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### livekraken-filter

```bash
$ singularity exec <container> /usr/local/bin/livekraken-filter
$ podman run --it --rm --entrypoint /usr/local/bin/livekraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/livekraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### livekraken-mpa-report

```bash
$ singularity exec <container> /usr/local/bin/livekraken-mpa-report
$ podman run --it --rm --entrypoint /usr/local/bin/livekraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/livekraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### livekraken-report

```bash
$ singularity exec <container> /usr/local/bin/livekraken-report
$ podman run --it --rm --entrypoint /usr/local/bin/livekraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/livekraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### livekraken-translate

```bash
$ singularity exec <container> /usr/local/bin/livekraken-translate
$ podman run --it --rm --entrypoint /usr/local/bin/livekraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/livekraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### livekraken_sankey_diagram.py

```bash
$ singularity exec <container> /usr/local/bin/livekraken_sankey_diagram.py
$ podman run --it --rm --entrypoint /usr/local/bin/livekraken_sankey_diagram.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/livekraken_sankey_diagram.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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