---
layout: container
name:  "quay.io/biocontainers/kipoi_veff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kipoi_veff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kipoi_veff/container.yaml"
updated_at: "2023-06-18 03:21:35.472060"
latest: "0.3.1--pyh145b6a8_1"
container_url: "https://biocontainers.pro/tools/kipoi_veff"
aliases:
 - "cookiecutter"
 - "ddls"
 - "kipoi"
 - "slugify"
 - "unidecode"
 - "cyvcf2"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "pbt_plotting_example.py"
 - "peak_pie.py"
 - "pybedtools"
 - "venn_gchart.py"
 - "venn_mpl.py"
 - "annotate.py"
versions:
 - "0.3.1--pyh145b6a8_1"
description: "shpc-registry automated BioContainers addition for kipoi_veff"
config: {"url": "https://biocontainers.pro/tools/kipoi_veff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kipoi_veff", "latest": {"0.3.1--pyh145b6a8_1": "sha256:5692353c0b9068f8dc3c755b95ca02e0206474b3d80657706a6ce6a71b402cb7"}, "tags": {"0.3.1--pyh145b6a8_1": "sha256:5692353c0b9068f8dc3c755b95ca02e0206474b3d80657706a6ce6a71b402cb7"}, "docker": "quay.io/biocontainers/kipoi_veff", "aliases": {"cookiecutter": "/usr/local/bin/cookiecutter", "ddls": "/usr/local/bin/ddls", "kipoi": "/usr/local/bin/kipoi", "slugify": "/usr/local/bin/slugify", "unidecode": "/usr/local/bin/unidecode", "cyvcf2": "/usr/local/bin/cyvcf2", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kipoi_veff.
shpc-registry automated BioContainers addition for kipoi_veff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kipoi_veff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kipoi_veff:0.3.1--pyh145b6a8_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kipoi_veff/0.3.1--pyh145b6a8_1
$ module help quay.io/biocontainers/kipoi_veff/0.3.1--pyh145b6a8_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kipoi_veff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kipoi_veff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kipoi_veff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kipoi_veff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kipoi_veff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kipoi_veff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cookiecutter

```bash
$ singularity exec <container> /usr/local/bin/cookiecutter
$ podman run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ddls

```bash
$ singularity exec <container> /usr/local/bin/ddls
$ podman run --it --rm --entrypoint /usr/local/bin/ddls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ddls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kipoi

```bash
$ singularity exec <container> /usr/local/bin/kipoi
$ podman run --it --rm --entrypoint /usr/local/bin/kipoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kipoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unidecode

```bash
$ singularity exec <container> /usr/local/bin/unidecode
$ podman run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersection_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/intersection_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron_exon_reads.py

```bash
$ singularity exec <container> /usr/local/bin/intron_exon_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbt_plotting_example.py

```bash
$ singularity exec <container> /usr/local/bin/pbt_plotting_example.py
$ podman run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peak_pie.py

```bash
$ singularity exec <container> /usr/local/bin/peak_pie.py
$ podman run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybedtools

```bash
$ singularity exec <container> /usr/local/bin/pybedtools
$ podman run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_gchart.py

```bash
$ singularity exec <container> /usr/local/bin/venn_gchart.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_mpl.py

```bash
$ singularity exec <container> /usr/local/bin/venn_mpl.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate.py

```bash
$ singularity exec <container> /usr/local/bin/annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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