---
layout: container
name:  "quay.io/biocontainers/probamconvert"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/probamconvert/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/probamconvert/container.yaml"
updated_at: "2024-05-21 02:33:45.145311"
latest: "1.0.2--2"
container_url: "https://biocontainers.pro/tools/probamconvert"
aliases:
 - "proBAM.py"
 - "proBAM_ENSEMBL.py"
 - "proBAM_GUI.py"
 - "proBAM_IDparser.py"
 - "proBAM_biomart.py"
 - "proBAM_coref.py"
 - "proBAM_input.py"
 - "proBAM_mzTab.py"
 - "proBAM_mzid.py"
 - "proBAM_pepxml.py"
 - "proBAM_proBED.py"
 - "easydev_buildPackage"
 - "ibrowse"
 - "multigit"
 - "browse"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "pybabel"
 - "aggregate_profile.pl"
versions:
 - "1.0.2--2"
description: "shpc-registry automated BioContainers addition for probamconvert"
config: {"url": "https://biocontainers.pro/tools/probamconvert", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for probamconvert", "latest": {"1.0.2--2": "sha256:166c6e14e70dd9163ac7d4a139d76f38d6a7d9d3fe87f994387293941eb6f8c2"}, "tags": {"1.0.2--2": "sha256:166c6e14e70dd9163ac7d4a139d76f38d6a7d9d3fe87f994387293941eb6f8c2"}, "docker": "quay.io/biocontainers/probamconvert", "aliases": {"proBAM.py": "/usr/local/bin/proBAM.py", "proBAM_ENSEMBL.py": "/usr/local/bin/proBAM_ENSEMBL.py", "proBAM_GUI.py": "/usr/local/bin/proBAM_GUI.py", "proBAM_IDparser.py": "/usr/local/bin/proBAM_IDparser.py", "proBAM_biomart.py": "/usr/local/bin/proBAM_biomart.py", "proBAM_coref.py": "/usr/local/bin/proBAM_coref.py", "proBAM_input.py": "/usr/local/bin/proBAM_input.py", "proBAM_mzTab.py": "/usr/local/bin/proBAM_mzTab.py", "proBAM_mzid.py": "/usr/local/bin/proBAM_mzid.py", "proBAM_pepxml.py": "/usr/local/bin/proBAM_pepxml.py", "proBAM_proBED.py": "/usr/local/bin/proBAM_proBED.py", "easydev_buildPackage": "/usr/local/bin/easydev_buildPackage", "ibrowse": "/usr/local/bin/ibrowse", "multigit": "/usr/local/bin/multigit", "browse": "/usr/local/bin/browse", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "pybabel": "/usr/local/bin/pybabel", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/probamconvert.
shpc-registry automated BioContainers addition for probamconvert
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/probamconvert
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/probamconvert:1.0.2--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/probamconvert/1.0.2--2
$ module help quay.io/biocontainers/probamconvert/1.0.2--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### probamconvert-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### probamconvert-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### probamconvert-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### probamconvert-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### probamconvert-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### probamconvert-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### proBAM.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_ENSEMBL.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_ENSEMBL.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_ENSEMBL.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_ENSEMBL.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_GUI.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_GUI.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_GUI.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_GUI.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_IDparser.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_IDparser.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_IDparser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_IDparser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_biomart.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_biomart.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_biomart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_biomart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_coref.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_coref.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_coref.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_coref.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_input.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_input.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_input.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_input.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_mzTab.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_mzTab.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_mzTab.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_mzTab.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_mzid.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_mzid.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_mzid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_mzid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_pepxml.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_pepxml.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_pepxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_pepxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proBAM_proBED.py

```bash
$ singularity exec <container> /usr/local/bin/proBAM_proBED.py
$ podman run --it --rm --entrypoint /usr/local/bin/proBAM_proBED.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proBAM_proBED.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easydev_buildPackage

```bash
$ singularity exec <container> /usr/local/bin/easydev_buildPackage
$ podman run --it --rm --entrypoint /usr/local/bin/easydev_buildPackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easydev_buildPackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibrowse

```bash
$ singularity exec <container> /usr/local/bin/ibrowse
$ podman run --it --rm --entrypoint /usr/local/bin/ibrowse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibrowse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multigit

```bash
$ singularity exec <container> /usr/local/bin/multigit
$ podman run --it --rm --entrypoint /usr/local/bin/multigit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multigit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### browse

```bash
$ singularity exec <container> /usr/local/bin/browse
$ podman run --it --rm --entrypoint /usr/local/bin/browse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/browse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-apidoc

```bash
$ singularity exec <container> /usr/local/bin/sphinx-apidoc
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-autogen

```bash
$ singularity exec <container> /usr/local/bin/sphinx-autogen
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-build

```bash
$ singularity exec <container> /usr/local/bin/sphinx-build
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-quickstart

```bash
$ singularity exec <container> /usr/local/bin/sphinx-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_profile.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregate_profile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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