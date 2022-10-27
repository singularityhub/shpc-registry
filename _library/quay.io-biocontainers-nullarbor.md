---
layout: container
name:  "quay.io/biocontainers/nullarbor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nullarbor/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nullarbor/container.yaml"
updated_at: "2022-10-27 01:05:02.630491"
latest: "2.0.20191013--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/nullarbor"
aliases:
 - "centrifuge_evaluate.py"
 - "centrifuge_simulate_reads.py"
 - "coronaspades.py"
 - "fa"
 - "fq"
 - "kraken2"
 - "kraken2-build"
 - "kraken2-inspect"
 - "metaplasmidspades.py"
 - "metaviralspades.py"
 - "nullarbor-json.pl"
 - "nullarbor-report.pl"
 - "nullarbor.pl"
 - "nw_clade"
 - "nw_condense"
 - "nw_display"
 - "nw_distance"
 - "nw_duration"
 - "nw_ed"
 - "nw_gen"
 - "nw_indent"
 - "nw_labels"
 - "nw_match"
 - "nw_order"
 - "nw_prune"
 - "nw_rename"
 - "nw_reroot"
 - "nw_stats"
 - "nw_support"
 - "nw_topology"
 - "nw_trim"
 - "quicktree"
 - "rnaviralspades.py"
 - "roary2svg.pl"
 - "shovill"
 - "snp-dists"
 - "split_ref_by_bai_datasize.py"
versions:
 - "2.0.20191013--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for nullarbor"
config: {"url": "https://biocontainers.pro/tools/nullarbor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nullarbor", "latest": {"2.0.20191013--hdfd78af_3": "sha256:c5ca9ba1519766198953ff6cd18cc9330ddb9a1c8498567a54d0538530bbff1f"}, "tags": {"2.0.20191013--hdfd78af_3": "sha256:c5ca9ba1519766198953ff6cd18cc9330ddb9a1c8498567a54d0538530bbff1f"}, "docker": "quay.io/biocontainers/nullarbor", "aliases": {"centrifuge_evaluate.py": "/usr/local/bin/centrifuge_evaluate.py", "centrifuge_simulate_reads.py": "/usr/local/bin/centrifuge_simulate_reads.py", "coronaspades.py": "/usr/local/bin/coronaspades.py", "fa": "/usr/local/bin/fa", "fq": "/usr/local/bin/fq", "kraken2": "/usr/local/bin/kraken2", "kraken2-build": "/usr/local/bin/kraken2-build", "kraken2-inspect": "/usr/local/bin/kraken2-inspect", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "nullarbor-json.pl": "/usr/local/bin/nullarbor-json.pl", "nullarbor-report.pl": "/usr/local/bin/nullarbor-report.pl", "nullarbor.pl": "/usr/local/bin/nullarbor.pl", "nw_clade": "/usr/local/bin/nw_clade", "nw_condense": "/usr/local/bin/nw_condense", "nw_display": "/usr/local/bin/nw_display", "nw_distance": "/usr/local/bin/nw_distance", "nw_duration": "/usr/local/bin/nw_duration", "nw_ed": "/usr/local/bin/nw_ed", "nw_gen": "/usr/local/bin/nw_gen", "nw_indent": "/usr/local/bin/nw_indent", "nw_labels": "/usr/local/bin/nw_labels", "nw_match": "/usr/local/bin/nw_match", "nw_order": "/usr/local/bin/nw_order", "nw_prune": "/usr/local/bin/nw_prune", "nw_rename": "/usr/local/bin/nw_rename", "nw_reroot": "/usr/local/bin/nw_reroot", "nw_stats": "/usr/local/bin/nw_stats", "nw_support": "/usr/local/bin/nw_support", "nw_topology": "/usr/local/bin/nw_topology", "nw_trim": "/usr/local/bin/nw_trim", "quicktree": "/usr/local/bin/quicktree", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "roary2svg.pl": "/usr/local/bin/roary2svg.pl", "shovill": "/usr/local/bin/shovill", "snp-dists": "/usr/local/bin/snp-dists", "split_ref_by_bai_datasize.py": "/usr/local/bin/split_ref_by_bai_datasize.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nullarbor.
shpc-registry automated BioContainers addition for nullarbor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nullarbor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nullarbor:2.0.20191013--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nullarbor/2.0.20191013--hdfd78af_3
$ module help quay.io/biocontainers/nullarbor/2.0.20191013--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nullarbor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nullarbor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nullarbor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nullarbor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nullarbor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nullarbor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### centrifuge_evaluate.py

```bash
$ singularity exec <container> /usr/local/bin/centrifuge_evaluate.py
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge_evaluate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge_evaluate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge_simulate_reads.py

```bash
$ singularity exec <container> /usr/local/bin/centrifuge_simulate_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coronaspades.py

```bash
$ singularity exec <container> /usr/local/bin/coronaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fa

```bash
$ singularity exec <container> /usr/local/bin/fa
$ podman run --it --rm --entrypoint /usr/local/bin/fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fq

```bash
$ singularity exec <container> /usr/local/bin/fq
$ podman run --it --rm --entrypoint /usr/local/bin/fq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2

```bash
$ singularity exec <container> /usr/local/bin/kraken2
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-build

```bash
$ singularity exec <container> /usr/local/bin/kraken2-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-inspect

```bash
$ singularity exec <container> /usr/local/bin/kraken2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaplasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaplasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nullarbor-json.pl

```bash
$ singularity exec <container> /usr/local/bin/nullarbor-json.pl
$ podman run --it --rm --entrypoint /usr/local/bin/nullarbor-json.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nullarbor-json.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nullarbor-report.pl

```bash
$ singularity exec <container> /usr/local/bin/nullarbor-report.pl
$ podman run --it --rm --entrypoint /usr/local/bin/nullarbor-report.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nullarbor-report.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nullarbor.pl

```bash
$ singularity exec <container> /usr/local/bin/nullarbor.pl
$ podman run --it --rm --entrypoint /usr/local/bin/nullarbor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nullarbor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_clade

```bash
$ singularity exec <container> /usr/local/bin/nw_clade
$ podman run --it --rm --entrypoint /usr/local/bin/nw_clade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_clade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_condense

```bash
$ singularity exec <container> /usr/local/bin/nw_condense
$ podman run --it --rm --entrypoint /usr/local/bin/nw_condense   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_condense   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_display

```bash
$ singularity exec <container> /usr/local/bin/nw_display
$ podman run --it --rm --entrypoint /usr/local/bin/nw_display   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_display   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_distance

```bash
$ singularity exec <container> /usr/local/bin/nw_distance
$ podman run --it --rm --entrypoint /usr/local/bin/nw_distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_duration

```bash
$ singularity exec <container> /usr/local/bin/nw_duration
$ podman run --it --rm --entrypoint /usr/local/bin/nw_duration   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_duration   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_ed

```bash
$ singularity exec <container> /usr/local/bin/nw_ed
$ podman run --it --rm --entrypoint /usr/local/bin/nw_ed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_ed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_gen

```bash
$ singularity exec <container> /usr/local/bin/nw_gen
$ podman run --it --rm --entrypoint /usr/local/bin/nw_gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_indent

```bash
$ singularity exec <container> /usr/local/bin/nw_indent
$ podman run --it --rm --entrypoint /usr/local/bin/nw_indent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_indent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_labels

```bash
$ singularity exec <container> /usr/local/bin/nw_labels
$ podman run --it --rm --entrypoint /usr/local/bin/nw_labels   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_labels   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_match

```bash
$ singularity exec <container> /usr/local/bin/nw_match
$ podman run --it --rm --entrypoint /usr/local/bin/nw_match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_order

```bash
$ singularity exec <container> /usr/local/bin/nw_order
$ podman run --it --rm --entrypoint /usr/local/bin/nw_order   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_order   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_prune

```bash
$ singularity exec <container> /usr/local/bin/nw_prune
$ podman run --it --rm --entrypoint /usr/local/bin/nw_prune   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_prune   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_rename

```bash
$ singularity exec <container> /usr/local/bin/nw_rename
$ podman run --it --rm --entrypoint /usr/local/bin/nw_rename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_rename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_reroot

```bash
$ singularity exec <container> /usr/local/bin/nw_reroot
$ podman run --it --rm --entrypoint /usr/local/bin/nw_reroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_reroot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_stats

```bash
$ singularity exec <container> /usr/local/bin/nw_stats
$ podman run --it --rm --entrypoint /usr/local/bin/nw_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_support

```bash
$ singularity exec <container> /usr/local/bin/nw_support
$ podman run --it --rm --entrypoint /usr/local/bin/nw_support   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_support   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_topology

```bash
$ singularity exec <container> /usr/local/bin/nw_topology
$ podman run --it --rm --entrypoint /usr/local/bin/nw_topology   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_topology   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nw_trim

```bash
$ singularity exec <container> /usr/local/bin/nw_trim
$ podman run --it --rm --entrypoint /usr/local/bin/nw_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nw_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quicktree

```bash
$ singularity exec <container> /usr/local/bin/quicktree
$ podman run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roary2svg.pl

```bash
$ singularity exec <container> /usr/local/bin/roary2svg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/roary2svg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roary2svg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shovill

```bash
$ singularity exec <container> /usr/local/bin/shovill
$ podman run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp-dists

```bash
$ singularity exec <container> /usr/local/bin/snp-dists
$ podman run --it --rm --entrypoint /usr/local/bin/snp-dists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-dists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_ref_by_bai_datasize.py

```bash
$ singularity exec <container> /usr/local/bin/split_ref_by_bai_datasize.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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