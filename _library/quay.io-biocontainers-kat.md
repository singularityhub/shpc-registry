---
layout: container
name:  "quay.io/biocontainers/kat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kat/container.yaml"
updated_at: "2025-03-13 03:11:40.220826"
latest: "2.4.2--py39h7c5ebd6_3"
container_url: "https://biocontainers.pro/tools/kat"
aliases:
 - "kat"
 - "kat_distanalysis"
 - "kat_jellyfish"
 - "kat_plot_cold"
 - "kat_plot_density"
 - "kat_plot_profile"
 - "kat_plot_spectra_cn"
 - "kat_plot_spectra_hist"
 - "kat_plot_spectra_mx"
 - "tabulate"
 - "f2py3.6"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
versions:
 - "2.4.2--py36h873903e_2"
 - "2.4.2--py39h7c5ebd6_3"
 - "2.4.2--py36hc902310_3"
description: "shpc-registry automated BioContainers addition for kat"
config: {"url": "https://biocontainers.pro/tools/kat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kat", "latest": {"2.4.2--py39h7c5ebd6_3": "sha256:a3f774bef166850cee064d97064afea39fd21f80b00786fd475e61cfe28a7372"}, "tags": {"2.4.2--py36h873903e_2": "sha256:74b2649ad063f0091c9f09602f7fee8d872a99a2f54382bbb3d825cc8de79de4", "2.4.2--py39h7c5ebd6_3": "sha256:a3f774bef166850cee064d97064afea39fd21f80b00786fd475e61cfe28a7372", "2.4.2--py36hc902310_3": "sha256:45d58b422767d90d4065ccb6d5b2279ef52c5ef6ce3be1eb6b429245a90093ef"}, "docker": "quay.io/biocontainers/kat", "aliases": {"kat": "/usr/local/bin/kat", "kat_distanalysis": "/usr/local/bin/kat_distanalysis", "kat_jellyfish": "/usr/local/bin/kat_jellyfish", "kat_plot_cold": "/usr/local/bin/kat_plot_cold", "kat_plot_density": "/usr/local/bin/kat_plot_density", "kat_plot_profile": "/usr/local/bin/kat_plot_profile", "kat_plot_spectra_cn": "/usr/local/bin/kat_plot_spectra_cn", "kat_plot_spectra_hist": "/usr/local/bin/kat_plot_spectra_hist", "kat_plot_spectra_mx": "/usr/local/bin/kat_plot_spectra_mx", "tabulate": "/usr/local/bin/tabulate", "f2py3.6": "/usr/local/bin/f2py3.6", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kat.
shpc-registry automated BioContainers addition for kat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kat:2.4.2--py39h7c5ebd6_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kat/2.4.2--py39h7c5ebd6_3
$ module help quay.io/biocontainers/kat/2.4.2--py39h7c5ebd6_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kat

```bash
$ singularity exec <container> /usr/local/bin/kat
$ podman run --it --rm --entrypoint /usr/local/bin/kat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kat_distanalysis

```bash
$ singularity exec <container> /usr/local/bin/kat_distanalysis
$ podman run --it --rm --entrypoint /usr/local/bin/kat_distanalysis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kat_distanalysis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kat_jellyfish

```bash
$ singularity exec <container> /usr/local/bin/kat_jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/kat_jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kat_jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kat_plot_cold

```bash
$ singularity exec <container> /usr/local/bin/kat_plot_cold
$ podman run --it --rm --entrypoint /usr/local/bin/kat_plot_cold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kat_plot_cold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kat_plot_density

```bash
$ singularity exec <container> /usr/local/bin/kat_plot_density
$ podman run --it --rm --entrypoint /usr/local/bin/kat_plot_density   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kat_plot_density   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kat_plot_profile

```bash
$ singularity exec <container> /usr/local/bin/kat_plot_profile
$ podman run --it --rm --entrypoint /usr/local/bin/kat_plot_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kat_plot_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kat_plot_spectra_cn

```bash
$ singularity exec <container> /usr/local/bin/kat_plot_spectra_cn
$ podman run --it --rm --entrypoint /usr/local/bin/kat_plot_spectra_cn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kat_plot_spectra_cn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kat_plot_spectra_hist

```bash
$ singularity exec <container> /usr/local/bin/kat_plot_spectra_hist
$ podman run --it --rm --entrypoint /usr/local/bin/kat_plot_spectra_hist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kat_plot_spectra_hist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kat_plot_spectra_mx

```bash
$ singularity exec <container> /usr/local/bin/kat_plot_spectra_mx
$ podman run --it --rm --entrypoint /usr/local/bin/kat_plot_spectra_mx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kat_plot_spectra_mx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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