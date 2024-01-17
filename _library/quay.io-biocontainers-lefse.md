---
layout: container
name:  "quay.io/biocontainers/lefse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lefse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lefse/container.yaml"
updated_at: "2024-01-17 02:46:53.521678"
latest: "1.1.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/lefse"
aliases:
 - "lefse2circlader.py"
 - "lefse_format_input.py"
 - "lefse_plot_cladogram.py"
 - "lefse_plot_features.py"
 - "lefse_plot_res.py"
 - "lefse_run.py"
 - "qiime2lefse.py"
 - "biom"
 - "mirror_server"
 - "mirror_server_stop"
 - "futurize"
 - "pasteurize"
 - "f2py3.9"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "h5clear"
versions:
 - "1.1.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for lefse"
config: {"url": "https://biocontainers.pro/tools/lefse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lefse", "latest": {"1.1.2--pyhdfd78af_0": "sha256:6d7acc8bae889c9dd32295783ef17e5c8b75d00a27012283ad95af3dcae7bc27"}, "tags": {"1.1.2--pyhdfd78af_0": "sha256:6d7acc8bae889c9dd32295783ef17e5c8b75d00a27012283ad95af3dcae7bc27"}, "docker": "quay.io/biocontainers/lefse", "aliases": {"lefse2circlader.py": "/usr/local/bin/lefse2circlader.py", "lefse_format_input.py": "/usr/local/bin/lefse_format_input.py", "lefse_plot_cladogram.py": "/usr/local/bin/lefse_plot_cladogram.py", "lefse_plot_features.py": "/usr/local/bin/lefse_plot_features.py", "lefse_plot_res.py": "/usr/local/bin/lefse_plot_res.py", "lefse_run.py": "/usr/local/bin/lefse_run.py", "qiime2lefse.py": "/usr/local/bin/qiime2lefse.py", "biom": "/usr/local/bin/biom", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "f2py3.9": "/usr/local/bin/f2py3.9", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "h5clear": "/usr/local/bin/h5clear"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lefse.
shpc-registry automated BioContainers addition for lefse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lefse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lefse:1.1.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lefse/1.1.2--pyhdfd78af_0
$ module help quay.io/biocontainers/lefse/1.1.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lefse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lefse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lefse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lefse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lefse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lefse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lefse2circlader.py

```bash
$ singularity exec <container> /usr/local/bin/lefse2circlader.py
$ podman run --it --rm --entrypoint /usr/local/bin/lefse2circlader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lefse2circlader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lefse_format_input.py

```bash
$ singularity exec <container> /usr/local/bin/lefse_format_input.py
$ podman run --it --rm --entrypoint /usr/local/bin/lefse_format_input.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lefse_format_input.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lefse_plot_cladogram.py

```bash
$ singularity exec <container> /usr/local/bin/lefse_plot_cladogram.py
$ podman run --it --rm --entrypoint /usr/local/bin/lefse_plot_cladogram.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lefse_plot_cladogram.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lefse_plot_features.py

```bash
$ singularity exec <container> /usr/local/bin/lefse_plot_features.py
$ podman run --it --rm --entrypoint /usr/local/bin/lefse_plot_features.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lefse_plot_features.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lefse_plot_res.py

```bash
$ singularity exec <container> /usr/local/bin/lefse_plot_res.py
$ podman run --it --rm --entrypoint /usr/local/bin/lefse_plot_res.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lefse_plot_res.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lefse_run.py

```bash
$ singularity exec <container> /usr/local/bin/lefse_run.py
$ podman run --it --rm --entrypoint /usr/local/bin/lefse_run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lefse_run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qiime2lefse.py

```bash
$ singularity exec <container> /usr/local/bin/qiime2lefse.py
$ podman run --it --rm --entrypoint /usr/local/bin/qiime2lefse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qiime2lefse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biom

```bash
$ singularity exec <container> /usr/local/bin/biom
$ podman run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server_stop

```bash
$ singularity exec <container> /usr/local/bin/mirror_server_stop
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
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