---
layout: container
name:  "quay.io/biocontainers/prophyle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prophyle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prophyle/container.yaml"
updated_at: "2024-07-07 03:16:10.768932"
latest: "0.3.3.2--py310hdf79db3_2"
container_url: "https://biocontainers.pro/tools/prophyle"
aliases:
 - "prophyle"
 - "prophyle_analyze.py"
 - "prophyle_assignment.py"
 - "prophyle_ncbi_tree.py"
 - "prophyle_otu_table.py"
 - "prophyle_paired_end.py"
 - "prophyle_plot_tree.py"
 - "prophyle_propagation_makefile.py"
 - "prophyle_propagation_postprocessing.py"
 - "prophyle_propagation_preprocessing.py"
 - "prophyle_split_allseq.py"
 - "ete3"
 - "compile-et.pl"
 - "prerr.properties"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
 - "f2py3.6"
 - "certutil"
 - "nspr-config"
 - "nss-config"
versions:
 - "0.3.1.0--py36h8b12597_5"
 - "0.3.3.1--py39h4e691d4_0"
 - "0.3.3.2--py310h6cc9453_1"
 - "0.3.3.2--py310hdf79db3_2"
description: "shpc-registry automated BioContainers addition for prophyle"
config: {"url": "https://biocontainers.pro/tools/prophyle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prophyle", "latest": {"0.3.3.2--py310hdf79db3_2": "sha256:7869c3bcf7067d14343b1a709d0156b179eb4e0898645252f44757beda0d400d"}, "tags": {"0.3.1.0--py36h8b12597_5": "sha256:66c48c5cc47ceb1560c660015418833a6749a915d31891e3c2eda5c93609af83", "0.3.3.1--py39h4e691d4_0": "sha256:673cd302cca6d863eb9fe7e4968b73b764b966cc41f4ddffc26150719f4e22f7", "0.3.3.2--py310h6cc9453_1": "sha256:7f576ea378949e69d7b7f5321e5ad3ca4328bd67c5046548c9f5a461b9cc0a44", "0.3.3.2--py310hdf79db3_2": "sha256:7869c3bcf7067d14343b1a709d0156b179eb4e0898645252f44757beda0d400d"}, "docker": "quay.io/biocontainers/prophyle", "aliases": {"prophyle": "/usr/local/bin/prophyle", "prophyle_analyze.py": "/usr/local/bin/prophyle_analyze.py", "prophyle_assignment.py": "/usr/local/bin/prophyle_assignment.py", "prophyle_ncbi_tree.py": "/usr/local/bin/prophyle_ncbi_tree.py", "prophyle_otu_table.py": "/usr/local/bin/prophyle_otu_table.py", "prophyle_paired_end.py": "/usr/local/bin/prophyle_paired_end.py", "prophyle_plot_tree.py": "/usr/local/bin/prophyle_plot_tree.py", "prophyle_propagation_makefile.py": "/usr/local/bin/prophyle_propagation_makefile.py", "prophyle_propagation_postprocessing.py": "/usr/local/bin/prophyle_propagation_postprocessing.py", "prophyle_propagation_preprocessing.py": "/usr/local/bin/prophyle_propagation_preprocessing.py", "prophyle_split_allseq.py": "/usr/local/bin/prophyle_split_allseq.py", "ete3": "/usr/local/bin/ete3", "compile-et.pl": "/usr/local/bin/compile-et.pl", "prerr.properties": "/usr/local/bin/prerr.properties", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen", "f2py3.6": "/usr/local/bin/f2py3.6", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prophyle.
shpc-registry automated BioContainers addition for prophyle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prophyle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prophyle:0.3.3.2--py310hdf79db3_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prophyle/0.3.3.2--py310hdf79db3_2
$ module help quay.io/biocontainers/prophyle/0.3.3.2--py310hdf79db3_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prophyle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prophyle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prophyle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prophyle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prophyle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prophyle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prophyle

```bash
$ singularity exec <container> /usr/local/bin/prophyle
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_analyze.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_analyze.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_analyze.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_analyze.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_assignment.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_assignment.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_assignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_assignment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_ncbi_tree.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_ncbi_tree.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_ncbi_tree.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_ncbi_tree.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_otu_table.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_otu_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_otu_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_otu_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_paired_end.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_paired_end.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_paired_end.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_paired_end.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_plot_tree.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_plot_tree.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_plot_tree.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_plot_tree.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_propagation_makefile.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_propagation_makefile.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_propagation_makefile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_propagation_makefile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_propagation_postprocessing.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_propagation_postprocessing.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_propagation_postprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_propagation_postprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_propagation_preprocessing.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_propagation_preprocessing.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_propagation_preprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_propagation_preprocessing.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prophyle_split_allseq.py

```bash
$ singularity exec <container> /usr/local/bin/prophyle_split_allseq.py
$ podman run --it --rm --entrypoint /usr/local/bin/prophyle_split_allseq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophyle_split_allseq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete3

```bash
$ singularity exec <container> /usr/local/bin/ete3
$ podman run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile-et.pl

```bash
$ singularity exec <container> /usr/local/bin/compile-et.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prerr.properties

```bash
$ singularity exec <container> /usr/local/bin/prerr.properties
$ podman run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### nss-config

```bash
$ singularity exec <container> /usr/local/bin/nss-config
$ podman run --it --rm --entrypoint /usr/local/bin/nss-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nss-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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