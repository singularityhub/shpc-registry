---
layout: container
name:  "ghcr.io/autamus/nco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/nco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/nco/container.yaml"
updated_at: "2024-09-10 02:44:08.284781"
latest: "5.0.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/nco"
aliases:
 - "nc-config"
 - "ncap2"
 - "ncatted"
 - "ncbo"
 - "ncclimo"
 - "nccopy"
 - "ncdiff"
 - "ncdump"
 - "ncea"
 - "ncecat"
 - "nces"
 - "ncflint"
 - "ncgen"
 - "ncgen3"
 - "ncks"
 - "ncpdq"
 - "ncra"
 - "ncrcat"
 - "ncremap"
 - "ncrename"
 - "ncurses6-config"
 - "ncursesw6-config"
 - "ncwa"
versions:
 - "4.9.8"
 - "4.9.9"
 - "5.0.0"
 - "5.0.1"
 - "5.0.3"
 - "latest"

config: {"docker": "ghcr.io/autamus/nco", "url": "https://github.com/orgs/autamus/packages/container/package/nco", "maintainer": "@vsoch", "description": "", "latest": {"5.0.3": "sha256:b06b237c4c115d986be3270c7959c8efc3acf0de037e702f10a40d87e0a32dca"}, "tags": {"4.9.8": "sha256:1e67403beaf3e7cac0b36aa43c8436f2111a3eb489b32271c2ffeb0b20e2ec5a", "4.9.9": "sha256:38c1b5a2a37e6966e095630da89767ba1bd9b20bb06098f273aacaf1840af357", "5.0.0": "sha256:77a49b866afd2ce0ee8ec493d406c70450ed89ecae009dd8857883caa962eb60", "5.0.1": "sha256:0135da1092b32aa49c55f85de72e34064610746aaa7ff85c003bef9d42660840", "5.0.3": "sha256:b06b237c4c115d986be3270c7959c8efc3acf0de037e702f10a40d87e0a32dca", "latest": "sha256:b06b237c4c115d986be3270c7959c8efc3acf0de037e702f10a40d87e0a32dca"}, "aliases": {"nc-config": "/opt/view/bin/nc-config", "ncap2": "/opt/view/bin/ncap2", "ncatted": "/opt/view/bin/ncatted", "ncbo": "/opt/view/bin/ncbo", "ncclimo": "/opt/view/bin/ncclimo", "nccopy": "/opt/view/bin/nccopy", "ncdiff": "/opt/view/bin/ncdiff", "ncdump": "/opt/view/bin/ncdump", "ncea": "/opt/view/bin/ncea", "ncecat": "/opt/view/bin/ncecat", "nces": "/opt/view/bin/nces", "ncflint": "/opt/view/bin/ncflint", "ncgen": "/opt/view/bin/ncgen", "ncgen3": "/opt/view/bin/ncgen3", "ncks": "/opt/view/bin/ncks", "ncpdq": "/opt/view/bin/ncpdq", "ncra": "/opt/view/bin/ncra", "ncrcat": "/opt/view/bin/ncrcat", "ncremap": "/opt/view/bin/ncremap", "ncrename": "/opt/view/bin/ncrename", "ncurses6-config": "/opt/view/bin/ncurses6-config", "ncursesw6-config": "/opt/view/bin/ncursesw6-config", "ncwa": "/opt/view/bin/ncwa"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/nco.

After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/nco
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/nco:5.0.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/nco/5.0.3
$ module help ghcr.io/autamus/nco/5.0.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nc-config

```bash
$ singularity exec <container> /opt/view/bin/nc-config
$ podman run --it --rm --entrypoint /opt/view/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncap2

```bash
$ singularity exec <container> /opt/view/bin/ncap2
$ podman run --it --rm --entrypoint /opt/view/bin/ncap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncatted

```bash
$ singularity exec <container> /opt/view/bin/ncatted
$ podman run --it --rm --entrypoint /opt/view/bin/ncatted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncatted   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbo

```bash
$ singularity exec <container> /opt/view/bin/ncbo
$ podman run --it --rm --entrypoint /opt/view/bin/ncbo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncbo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncclimo

```bash
$ singularity exec <container> /opt/view/bin/ncclimo
$ podman run --it --rm --entrypoint /opt/view/bin/ncclimo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncclimo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nccopy

```bash
$ singularity exec <container> /opt/view/bin/nccopy
$ podman run --it --rm --entrypoint /opt/view/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncdiff

```bash
$ singularity exec <container> /opt/view/bin/ncdiff
$ podman run --it --rm --entrypoint /opt/view/bin/ncdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncdump

```bash
$ singularity exec <container> /opt/view/bin/ncdump
$ podman run --it --rm --entrypoint /opt/view/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncea

```bash
$ singularity exec <container> /opt/view/bin/ncea
$ podman run --it --rm --entrypoint /opt/view/bin/ncea   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncea   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncecat

```bash
$ singularity exec <container> /opt/view/bin/ncecat
$ podman run --it --rm --entrypoint /opt/view/bin/ncecat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncecat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nces

```bash
$ singularity exec <container> /opt/view/bin/nces
$ podman run --it --rm --entrypoint /opt/view/bin/nces   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/nces   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncflint

```bash
$ singularity exec <container> /opt/view/bin/ncflint
$ podman run --it --rm --entrypoint /opt/view/bin/ncflint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncflint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen

```bash
$ singularity exec <container> /opt/view/bin/ncgen
$ podman run --it --rm --entrypoint /opt/view/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen3

```bash
$ singularity exec <container> /opt/view/bin/ncgen3
$ podman run --it --rm --entrypoint /opt/view/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncks

```bash
$ singularity exec <container> /opt/view/bin/ncks
$ podman run --it --rm --entrypoint /opt/view/bin/ncks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncpdq

```bash
$ singularity exec <container> /opt/view/bin/ncpdq
$ podman run --it --rm --entrypoint /opt/view/bin/ncpdq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncpdq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncra

```bash
$ singularity exec <container> /opt/view/bin/ncra
$ podman run --it --rm --entrypoint /opt/view/bin/ncra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncra   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrcat

```bash
$ singularity exec <container> /opt/view/bin/ncrcat
$ podman run --it --rm --entrypoint /opt/view/bin/ncrcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncrcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncremap

```bash
$ singularity exec <container> /opt/view/bin/ncremap
$ podman run --it --rm --entrypoint /opt/view/bin/ncremap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncremap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrename

```bash
$ singularity exec <container> /opt/view/bin/ncrename
$ podman run --it --rm --entrypoint /opt/view/bin/ncrename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncrename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses6-config

```bash
$ singularity exec <container> /opt/view/bin/ncurses6-config
$ podman run --it --rm --entrypoint /opt/view/bin/ncurses6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncurses6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw6-config

```bash
$ singularity exec <container> /opt/view/bin/ncursesw6-config
$ podman run --it --rm --entrypoint /opt/view/bin/ncursesw6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncursesw6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncwa

```bash
$ singularity exec <container> /opt/view/bin/ncwa
$ podman run --it --rm --entrypoint /opt/view/bin/ncwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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