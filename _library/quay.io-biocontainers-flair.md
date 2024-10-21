---
layout: container
name:  "quay.io/biocontainers/flair"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flair/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/flair/container.yaml"
updated_at: "2024-10-21 03:37:52.566445"
latest: "2.0.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/flair"
aliases:
 - "bam2Bed12"
 - "bed_to_psl"
 - "deFLAIR"
 - "diff_iso_usage"
 - "diffsplice_fishers_exact"
 - "flair"
 - "junctions_from_sam"
 - "mark_intron_retention"
 - "mark_productivity"
 - "normalize_counts_matrix"
 - "plot_isoform_usage"
 - "predictProductivity"
 - "psl_to_bed"
 - "psl_to_sequence"
 - "sam_to_map"
 - "minimap2.py"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "tqdm"
versions:
 - "1.6.4--pyhdfd78af_0"
 - "1.7.0--pyhdfd78af_1"
 - "2.0.0--pyhdfd78af_0"
 - "2.0.0--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for flair"
config: {"url": "https://biocontainers.pro/tools/flair", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flair", "latest": {"2.0.0--pyhdfd78af_1": "sha256:daf1b32daa11dfb022d2e499bffb5beb6f9e2682edeeace311d2226e0b224d9b"}, "tags": {"1.6.4--pyhdfd78af_0": "sha256:5de2354fa7fe9cb8e65048f82ca4bbb190bc813c74ffc60cc1df12f02d0b87b8", "1.7.0--pyhdfd78af_1": "sha256:f464d910b59ec4f0543b2b9dc1573bf78b6275c82b196ceecfeabb1399194cb3", "2.0.0--pyhdfd78af_0": "sha256:a36a1d3ad8defa14af4a76496df2dda7c334201ce17e6260b7e199b362f1534a", "2.0.0--pyhdfd78af_1": "sha256:daf1b32daa11dfb022d2e499bffb5beb6f9e2682edeeace311d2226e0b224d9b"}, "docker": "quay.io/biocontainers/flair", "aliases": {"bam2Bed12": "/usr/local/bin/bam2Bed12", "bed_to_psl": "/usr/local/bin/bed_to_psl", "deFLAIR": "/usr/local/bin/deFLAIR", "diff_iso_usage": "/usr/local/bin/diff_iso_usage", "diffsplice_fishers_exact": "/usr/local/bin/diffsplice_fishers_exact", "flair": "/usr/local/bin/flair", "junctions_from_sam": "/usr/local/bin/junctions_from_sam", "mark_intron_retention": "/usr/local/bin/mark_intron_retention", "mark_productivity": "/usr/local/bin/mark_productivity", "normalize_counts_matrix": "/usr/local/bin/normalize_counts_matrix", "plot_isoform_usage": "/usr/local/bin/plot_isoform_usage", "predictProductivity": "/usr/local/bin/predictProductivity", "psl_to_bed": "/usr/local/bin/psl_to_bed", "psl_to_sequence": "/usr/local/bin/psl_to_sequence", "sam_to_map": "/usr/local/bin/sam_to_map", "minimap2.py": "/usr/local/bin/minimap2.py", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "tqdm": "/usr/local/bin/tqdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flair.
shpc-registry automated BioContainers addition for flair
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flair
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flair:2.0.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flair/2.0.0--pyhdfd78af_1
$ module help quay.io/biocontainers/flair/2.0.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flair-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flair-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flair-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flair-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flair-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flair-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2Bed12

```bash
$ singularity exec <container> /usr/local/bin/bam2Bed12
$ podman run --it --rm --entrypoint /usr/local/bin/bam2Bed12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2Bed12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed_to_psl

```bash
$ singularity exec <container> /usr/local/bin/bed_to_psl
$ podman run --it --rm --entrypoint /usr/local/bin/bed_to_psl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed_to_psl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deFLAIR

```bash
$ singularity exec <container> /usr/local/bin/deFLAIR
$ podman run --it --rm --entrypoint /usr/local/bin/deFLAIR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deFLAIR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diff_iso_usage

```bash
$ singularity exec <container> /usr/local/bin/diff_iso_usage
$ podman run --it --rm --entrypoint /usr/local/bin/diff_iso_usage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diff_iso_usage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diffsplice_fishers_exact

```bash
$ singularity exec <container> /usr/local/bin/diffsplice_fishers_exact
$ podman run --it --rm --entrypoint /usr/local/bin/diffsplice_fishers_exact   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diffsplice_fishers_exact   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flair

```bash
$ singularity exec <container> /usr/local/bin/flair
$ podman run --it --rm --entrypoint /usr/local/bin/flair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### junctions_from_sam

```bash
$ singularity exec <container> /usr/local/bin/junctions_from_sam
$ podman run --it --rm --entrypoint /usr/local/bin/junctions_from_sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/junctions_from_sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mark_intron_retention

```bash
$ singularity exec <container> /usr/local/bin/mark_intron_retention
$ podman run --it --rm --entrypoint /usr/local/bin/mark_intron_retention   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mark_intron_retention   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mark_productivity

```bash
$ singularity exec <container> /usr/local/bin/mark_productivity
$ podman run --it --rm --entrypoint /usr/local/bin/mark_productivity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mark_productivity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize_counts_matrix

```bash
$ singularity exec <container> /usr/local/bin/normalize_counts_matrix
$ podman run --it --rm --entrypoint /usr/local/bin/normalize_counts_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize_counts_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_isoform_usage

```bash
$ singularity exec <container> /usr/local/bin/plot_isoform_usage
$ podman run --it --rm --entrypoint /usr/local/bin/plot_isoform_usage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_isoform_usage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### predictProductivity

```bash
$ singularity exec <container> /usr/local/bin/predictProductivity
$ podman run --it --rm --entrypoint /usr/local/bin/predictProductivity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/predictProductivity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl_to_bed

```bash
$ singularity exec <container> /usr/local/bin/psl_to_bed
$ podman run --it --rm --entrypoint /usr/local/bin/psl_to_bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl_to_bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl_to_sequence

```bash
$ singularity exec <container> /usr/local/bin/psl_to_sequence
$ podman run --it --rm --entrypoint /usr/local/bin/psl_to_sequence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl_to_sequence   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_to_map

```bash
$ singularity exec <container> /usr/local/bin/sam_to_map
$ podman run --it --rm --entrypoint /usr/local/bin/sam_to_map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_to_map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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