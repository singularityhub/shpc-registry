---
layout: container
name:  "quay.io/biocontainers/oncogemini"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oncogemini/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/oncogemini/container.yaml"
updated_at: "2023-11-20 02:55:35.615518"
latest: "1.0.0--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/oncogemini"
aliases:
 - "oncogemini"
 - "peddy"
 - "toolshed"
 - "vcf2db.py"
 - "vcfanno"
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
 - "1.0.0--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for oncogemini"
config: {"url": "https://biocontainers.pro/tools/oncogemini", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for oncogemini", "latest": {"1.0.0--pyh3252c3a_0": "sha256:833ad1c2cfa1b7aa6d61f000d4de7f8ed9bc86c9e579f99b8852b7f7d1de76bd"}, "tags": {"1.0.0--pyh3252c3a_0": "sha256:833ad1c2cfa1b7aa6d61f000d4de7f8ed9bc86c9e579f99b8852b7f7d1de76bd"}, "docker": "quay.io/biocontainers/oncogemini", "aliases": {"oncogemini": "/usr/local/bin/oncogemini", "peddy": "/usr/local/bin/peddy", "toolshed": "/usr/local/bin/toolshed", "vcf2db.py": "/usr/local/bin/vcf2db.py", "vcfanno": "/usr/local/bin/vcfanno", "unidecode": "/usr/local/bin/unidecode", "cyvcf2": "/usr/local/bin/cyvcf2", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oncogemini.
shpc-registry automated BioContainers addition for oncogemini
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oncogemini
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oncogemini:1.0.0--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oncogemini/1.0.0--pyh3252c3a_0
$ module help quay.io/biocontainers/oncogemini/1.0.0--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oncogemini-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oncogemini-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oncogemini-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oncogemini-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oncogemini-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oncogemini-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### oncogemini

```bash
$ singularity exec <container> /usr/local/bin/oncogemini
$ podman run --it --rm --entrypoint /usr/local/bin/oncogemini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oncogemini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peddy

```bash
$ singularity exec <container> /usr/local/bin/peddy
$ podman run --it --rm --entrypoint /usr/local/bin/peddy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peddy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toolshed

```bash
$ singularity exec <container> /usr/local/bin/toolshed
$ podman run --it --rm --entrypoint /usr/local/bin/toolshed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toolshed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2db.py

```bash
$ singularity exec <container> /usr/local/bin/vcf2db.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfanno

```bash
$ singularity exec <container> /usr/local/bin/vcfanno
$ podman run --it --rm --entrypoint /usr/local/bin/vcfanno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfanno   -v ${PWD} -w ${PWD} <container> -c " $@"
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