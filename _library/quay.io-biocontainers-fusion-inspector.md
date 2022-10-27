---
layout: container
name:  "quay.io/biocontainers/fusion-inspector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fusion-inspector/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fusion-inspector/container.yaml"
updated_at: "2022-10-27 00:31:28.028357"
latest: "2.2.1--py37pl526hdbffeaa_0"
container_url: "https://biocontainers.pro/tools/fusion-inspector"
aliases:
 - ".fusion-inspector-post-link.sh"
 - "FusionInspector"
 - "Trinity_gene_splice_modeler.py"
 - "analyze_diff_expr.pl"
 - "contig_ExN50_statistic.pl"
 - "define_clusters_by_cutting_tree.pl"
 - "extract_supertranscript_from_reference.py"
 - "filter_low_expr_transcripts.pl"
 - "get_Trinity_gene_to_trans_map.pl"
 - "gmap_compress"
 - "gmap_reassemble"
 - "gmap_uncompress"
 - "seqtk-trinity"
 - "sift_bam_max_cov.pl"
versions:
 - "2.2.1--py37pl526hdbffeaa_0"
description: "shpc-registry automated BioContainers addition for fusion-inspector"
config: {"url": "https://biocontainers.pro/tools/fusion-inspector", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fusion-inspector", "latest": {"2.2.1--py37pl526hdbffeaa_0": "sha256:7a4f52bbad27f0504680bb82ae74081e97a404f6e0b8a6a1b900ebdbbdb3b350"}, "tags": {"2.2.1--py37pl526hdbffeaa_0": "sha256:7a4f52bbad27f0504680bb82ae74081e97a404f6e0b8a6a1b900ebdbbdb3b350"}, "docker": "quay.io/biocontainers/fusion-inspector", "aliases": {".fusion-inspector-post-link.sh": "/usr/local/bin/.fusion-inspector-post-link.sh", "FusionInspector": "/usr/local/bin/FusionInspector", "Trinity_gene_splice_modeler.py": "/usr/local/bin/Trinity_gene_splice_modeler.py", "analyze_diff_expr.pl": "/usr/local/bin/analyze_diff_expr.pl", "contig_ExN50_statistic.pl": "/usr/local/bin/contig_ExN50_statistic.pl", "define_clusters_by_cutting_tree.pl": "/usr/local/bin/define_clusters_by_cutting_tree.pl", "extract_supertranscript_from_reference.py": "/usr/local/bin/extract_supertranscript_from_reference.py", "filter_low_expr_transcripts.pl": "/usr/local/bin/filter_low_expr_transcripts.pl", "get_Trinity_gene_to_trans_map.pl": "/usr/local/bin/get_Trinity_gene_to_trans_map.pl", "gmap_compress": "/usr/local/bin/gmap_compress", "gmap_reassemble": "/usr/local/bin/gmap_reassemble", "gmap_uncompress": "/usr/local/bin/gmap_uncompress", "seqtk-trinity": "/usr/local/bin/seqtk-trinity", "sift_bam_max_cov.pl": "/usr/local/bin/sift_bam_max_cov.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fusion-inspector.
shpc-registry automated BioContainers addition for fusion-inspector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fusion-inspector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fusion-inspector:2.2.1--py37pl526hdbffeaa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fusion-inspector/2.2.1--py37pl526hdbffeaa_0
$ module help quay.io/biocontainers/fusion-inspector/2.2.1--py37pl526hdbffeaa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fusion-inspector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fusion-inspector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fusion-inspector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fusion-inspector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fusion-inspector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fusion-inspector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .fusion-inspector-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.fusion-inspector-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.fusion-inspector-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.fusion-inspector-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FusionInspector

```bash
$ singularity exec <container> /usr/local/bin/FusionInspector
$ podman run --it --rm --entrypoint /usr/local/bin/FusionInspector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FusionInspector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Trinity_gene_splice_modeler.py

```bash
$ singularity exec <container> /usr/local/bin/Trinity_gene_splice_modeler.py
$ podman run --it --rm --entrypoint /usr/local/bin/Trinity_gene_splice_modeler.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Trinity_gene_splice_modeler.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyze_diff_expr.pl

```bash
$ singularity exec <container> /usr/local/bin/analyze_diff_expr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/analyze_diff_expr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyze_diff_expr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contig_ExN50_statistic.pl

```bash
$ singularity exec <container> /usr/local/bin/contig_ExN50_statistic.pl
$ podman run --it --rm --entrypoint /usr/local/bin/contig_ExN50_statistic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contig_ExN50_statistic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### define_clusters_by_cutting_tree.pl

```bash
$ singularity exec <container> /usr/local/bin/define_clusters_by_cutting_tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/define_clusters_by_cutting_tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/define_clusters_by_cutting_tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_supertranscript_from_reference.py

```bash
$ singularity exec <container> /usr/local/bin/extract_supertranscript_from_reference.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_supertranscript_from_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_supertranscript_from_reference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_low_expr_transcripts.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_low_expr_transcripts.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_low_expr_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_low_expr_transcripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_Trinity_gene_to_trans_map.pl

```bash
$ singularity exec <container> /usr/local/bin/get_Trinity_gene_to_trans_map.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_Trinity_gene_to_trans_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_Trinity_gene_to_trans_map.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_compress

```bash
$ singularity exec <container> /usr/local/bin/gmap_compress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_reassemble

```bash
$ singularity exec <container> /usr/local/bin/gmap_reassemble
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_uncompress

```bash
$ singularity exec <container> /usr/local/bin/gmap_uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtk-trinity

```bash
$ singularity exec <container> /usr/local/bin/seqtk-trinity
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk-trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk-trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sift_bam_max_cov.pl

```bash
$ singularity exec <container> /usr/local/bin/sift_bam_max_cov.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sift_bam_max_cov.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sift_bam_max_cov.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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