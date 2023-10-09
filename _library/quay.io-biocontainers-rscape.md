---
layout: container
name:  "quay.io/biocontainers/rscape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rscape/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rscape/container.yaml"
updated_at: "2023-10-09 02:34:20.139904"
latest: "1.4.0--hdbdd923_4"
container_url: "https://biocontainers.pro/tools/rscape"
aliases:
 - "FUNCS.pm"
 - "MetamakeDemos.pl"
 - "PDBFUNCS.pm"
 - "R-scape"
 - "R-scape-sim"
 - "R-scape-sim-nobps"
 - "R-view"
 - "SelectSubFamilyFromStockholm.pl"
 - "Stockholm.pm"
 - "appcov"
 - "msafilter"
 - "pdb_parse.pl"
 - "r2r"
 - "r2r_msa_comply.pl"
 - "chrpath"
 - "gnuplot"
 - "FastTree"
 - "xkbcli"
 - "pg_config"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
 - "certutil"
 - "nspr-config"
versions:
 - "1.4.0--h87f3376_2"
 - "1.4.0--hdbdd923_4"
description: "shpc-registry automated BioContainers addition for rscape"
config: {"url": "https://biocontainers.pro/tools/rscape", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rscape", "latest": {"1.4.0--hdbdd923_4": "sha256:c70e5b9a161c9fa5d035b807d8cffb4105c3b5d343f4b520ce318c5a2e30575d"}, "tags": {"1.4.0--h87f3376_2": "sha256:9d7f7ca8dba7431034a3725490de563b7c744dd6f36cc1bfee66a66be89c2b4b", "1.4.0--hdbdd923_4": "sha256:c70e5b9a161c9fa5d035b807d8cffb4105c3b5d343f4b520ce318c5a2e30575d"}, "docker": "quay.io/biocontainers/rscape", "aliases": {"FUNCS.pm": "/usr/local/bin/FUNCS.pm", "MetamakeDemos.pl": "/usr/local/bin/MetamakeDemos.pl", "PDBFUNCS.pm": "/usr/local/bin/PDBFUNCS.pm", "R-scape": "/usr/local/bin/R-scape", "R-scape-sim": "/usr/local/bin/R-scape-sim", "R-scape-sim-nobps": "/usr/local/bin/R-scape-sim-nobps", "R-view": "/usr/local/bin/R-view", "SelectSubFamilyFromStockholm.pl": "/usr/local/bin/SelectSubFamilyFromStockholm.pl", "Stockholm.pm": "/usr/local/bin/Stockholm.pm", "appcov": "/usr/local/bin/appcov", "msafilter": "/usr/local/bin/msafilter", "pdb_parse.pl": "/usr/local/bin/pdb_parse.pl", "r2r": "/usr/local/bin/r2r", "r2r_msa_comply.pl": "/usr/local/bin/r2r_msa_comply.pl", "chrpath": "/usr/local/bin/chrpath", "gnuplot": "/usr/local/bin/gnuplot", "FastTree": "/usr/local/bin/FastTree", "xkbcli": "/usr/local/bin/xkbcli", "pg_config": "/usr/local/bin/pg_config", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rscape.
shpc-registry automated BioContainers addition for rscape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rscape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rscape:1.4.0--hdbdd923_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rscape/1.4.0--hdbdd923_4
$ module help quay.io/biocontainers/rscape/1.4.0--hdbdd923_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rscape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rscape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rscape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rscape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rscape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rscape-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FUNCS.pm

```bash
$ singularity exec <container> /usr/local/bin/FUNCS.pm
$ podman run --it --rm --entrypoint /usr/local/bin/FUNCS.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FUNCS.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetamakeDemos.pl

```bash
$ singularity exec <container> /usr/local/bin/MetamakeDemos.pl
$ podman run --it --rm --entrypoint /usr/local/bin/MetamakeDemos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetamakeDemos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PDBFUNCS.pm

```bash
$ singularity exec <container> /usr/local/bin/PDBFUNCS.pm
$ podman run --it --rm --entrypoint /usr/local/bin/PDBFUNCS.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PDBFUNCS.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### R-scape

```bash
$ singularity exec <container> /usr/local/bin/R-scape
$ podman run --it --rm --entrypoint /usr/local/bin/R-scape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R-scape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### R-scape-sim

```bash
$ singularity exec <container> /usr/local/bin/R-scape-sim
$ podman run --it --rm --entrypoint /usr/local/bin/R-scape-sim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R-scape-sim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### R-scape-sim-nobps

```bash
$ singularity exec <container> /usr/local/bin/R-scape-sim-nobps
$ podman run --it --rm --entrypoint /usr/local/bin/R-scape-sim-nobps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R-scape-sim-nobps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### R-view

```bash
$ singularity exec <container> /usr/local/bin/R-view
$ podman run --it --rm --entrypoint /usr/local/bin/R-view   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R-view   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SelectSubFamilyFromStockholm.pl

```bash
$ singularity exec <container> /usr/local/bin/SelectSubFamilyFromStockholm.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SelectSubFamilyFromStockholm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SelectSubFamilyFromStockholm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Stockholm.pm

```bash
$ singularity exec <container> /usr/local/bin/Stockholm.pm
$ podman run --it --rm --entrypoint /usr/local/bin/Stockholm.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Stockholm.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appcov

```bash
$ singularity exec <container> /usr/local/bin/appcov
$ podman run --it --rm --entrypoint /usr/local/bin/appcov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appcov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msafilter

```bash
$ singularity exec <container> /usr/local/bin/msafilter
$ podman run --it --rm --entrypoint /usr/local/bin/msafilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msafilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_parse.pl

```bash
$ singularity exec <container> /usr/local/bin/pdb_parse.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_parse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_parse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### r2r

```bash
$ singularity exec <container> /usr/local/bin/r2r
$ podman run --it --rm --entrypoint /usr/local/bin/r2r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/r2r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### r2r_msa_comply.pl

```bash
$ singularity exec <container> /usr/local/bin/r2r_msa_comply.pl
$ podman run --it --rm --entrypoint /usr/local/bin/r2r_msa_comply.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/r2r_msa_comply.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chrpath

```bash
$ singularity exec <container> /usr/local/bin/chrpath
$ podman run --it --rm --entrypoint /usr/local/bin/chrpath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chrpath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnuplot

```bash
$ singularity exec <container> /usr/local/bin/gnuplot
$ podman run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_config

```bash
$ singularity exec <container> /usr/local/bin/pg_config
$ podman run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdistancefieldgenerator

```bash
$ singularity exec <container> /usr/local/bin/qdistancefieldgenerator
$ podman run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlpreview

```bash
$ singularity exec <container> /usr/local/bin/qmlpreview
$ podman run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvkgen

```bash
$ singularity exec <container> /usr/local/bin/qvkgen
$ podman run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certutil

```bash
$ singularity exec <container> /usr/local/bin/certutil
$ podman run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nspr-config

```bash
$ singularity exec <container> /usr/local/bin/nspr-config
$ podman run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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