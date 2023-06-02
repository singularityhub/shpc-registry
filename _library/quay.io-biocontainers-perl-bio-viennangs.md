---
layout: container
name:  "quay.io/biocontainers/perl-bio-viennangs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-viennangs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-viennangs/container.yaml"
updated_at: "2023-06-02 03:42:50.800412"
latest: "v0.19.2--pl526_5"
container_url: "https://biocontainers.pro/tools/perl-bio-viennangs"
aliases:
 - "Tutorial_pipeline03.pl"
 - "assembly_hub_constructor.pl"
 - "bam_split.pl"
 - "bam_to_bigwig.pl"
 - "bam_uniq.pl"
 - "bed2bedGraph.pl"
 - "bed2nt2aa.pl"
 - "bed62bed12.pl"
 - "fasta_multigrep.pl"
 - "fasta_regex.pl"
 - "fasta_subgrep.pl"
 - "fetchChromSizes"
 - "gff2bed.pl"
 - "kmer_analysis.pl"
 - "newUCSCdb.pl"
 - "normalize_multicov.pl"
 - "rnaseq_peakfinder.pl"
 - "sj_visualizer.pl"
 - "splice_site_summary.pl"
 - "track_hub_constructor.pl"
 - "trim_fastq.pl"
 - "pod_cover"
 - "bedGraphToBigWig"
 - "bedToBigBed"
 - "faToTwoBit"
 - "gifecho"
 - "gifinto"
 - "gdlib-config"
 - "bam2bedgraph"
 - "bp_find-blast-matches.pl"
 - "ace.pl"
versions:
 - "v0.19.2--pl526_5"
description: "shpc-registry automated BioContainers addition for perl-bio-viennangs"
config: {"url": "https://biocontainers.pro/tools/perl-bio-viennangs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-viennangs", "latest": {"v0.19.2--pl526_5": "sha256:de43ecda3071ccd279a0b9ae7a4355696f77cf453a1789e3e3b2588dd7e165fa"}, "tags": {"v0.19.2--pl526_5": "sha256:de43ecda3071ccd279a0b9ae7a4355696f77cf453a1789e3e3b2588dd7e165fa"}, "docker": "quay.io/biocontainers/perl-bio-viennangs", "aliases": {"Tutorial_pipeline03.pl": "/usr/local/bin/Tutorial_pipeline03.pl", "assembly_hub_constructor.pl": "/usr/local/bin/assembly_hub_constructor.pl", "bam_split.pl": "/usr/local/bin/bam_split.pl", "bam_to_bigwig.pl": "/usr/local/bin/bam_to_bigwig.pl", "bam_uniq.pl": "/usr/local/bin/bam_uniq.pl", "bed2bedGraph.pl": "/usr/local/bin/bed2bedGraph.pl", "bed2nt2aa.pl": "/usr/local/bin/bed2nt2aa.pl", "bed62bed12.pl": "/usr/local/bin/bed62bed12.pl", "fasta_multigrep.pl": "/usr/local/bin/fasta_multigrep.pl", "fasta_regex.pl": "/usr/local/bin/fasta_regex.pl", "fasta_subgrep.pl": "/usr/local/bin/fasta_subgrep.pl", "fetchChromSizes": "/usr/local/bin/fetchChromSizes", "gff2bed.pl": "/usr/local/bin/gff2bed.pl", "kmer_analysis.pl": "/usr/local/bin/kmer_analysis.pl", "newUCSCdb.pl": "/usr/local/bin/newUCSCdb.pl", "normalize_multicov.pl": "/usr/local/bin/normalize_multicov.pl", "rnaseq_peakfinder.pl": "/usr/local/bin/rnaseq_peakfinder.pl", "sj_visualizer.pl": "/usr/local/bin/sj_visualizer.pl", "splice_site_summary.pl": "/usr/local/bin/splice_site_summary.pl", "track_hub_constructor.pl": "/usr/local/bin/track_hub_constructor.pl", "trim_fastq.pl": "/usr/local/bin/trim_fastq.pl", "pod_cover": "/usr/local/bin/pod_cover", "bedGraphToBigWig": "/usr/local/bin/bedGraphToBigWig", "bedToBigBed": "/usr/local/bin/bedToBigBed", "faToTwoBit": "/usr/local/bin/faToTwoBit", "gifecho": "/usr/local/bin/gifecho", "gifinto": "/usr/local/bin/gifinto", "gdlib-config": "/usr/local/bin/gdlib-config", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "ace.pl": "/usr/local/bin/ace.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-viennangs.
shpc-registry automated BioContainers addition for perl-bio-viennangs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-viennangs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-viennangs:v0.19.2--pl526_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-viennangs/v0.19.2--pl526_5
$ module help quay.io/biocontainers/perl-bio-viennangs/v0.19.2--pl526_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-viennangs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-viennangs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-viennangs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-viennangs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-viennangs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-viennangs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Tutorial_pipeline03.pl

```bash
$ singularity exec <container> /usr/local/bin/Tutorial_pipeline03.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Tutorial_pipeline03.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Tutorial_pipeline03.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assembly_hub_constructor.pl

```bash
$ singularity exec <container> /usr/local/bin/assembly_hub_constructor.pl
$ podman run --it --rm --entrypoint /usr/local/bin/assembly_hub_constructor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assembly_hub_constructor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_split.pl

```bash
$ singularity exec <container> /usr/local/bin/bam_split.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bam_split.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_split.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_to_bigwig.pl

```bash
$ singularity exec <container> /usr/local/bin/bam_to_bigwig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bam_to_bigwig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_to_bigwig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_uniq.pl

```bash
$ singularity exec <container> /usr/local/bin/bam_uniq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bam_uniq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_uniq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2bedGraph.pl

```bash
$ singularity exec <container> /usr/local/bin/bed2bedGraph.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bed2bedGraph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2bedGraph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2nt2aa.pl

```bash
$ singularity exec <container> /usr/local/bin/bed2nt2aa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bed2nt2aa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2nt2aa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed62bed12.pl

```bash
$ singularity exec <container> /usr/local/bin/bed62bed12.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bed62bed12.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed62bed12.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_multigrep.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta_multigrep.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_multigrep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_multigrep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_regex.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta_regex.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_regex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_regex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_subgrep.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta_subgrep.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_subgrep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_subgrep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchChromSizes

```bash
$ singularity exec <container> /usr/local/bin/fetchChromSizes
$ podman run --it --rm --entrypoint /usr/local/bin/fetchChromSizes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchChromSizes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/gff2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer_analysis.pl

```bash
$ singularity exec <container> /usr/local/bin/kmer_analysis.pl
$ podman run --it --rm --entrypoint /usr/local/bin/kmer_analysis.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer_analysis.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### newUCSCdb.pl

```bash
$ singularity exec <container> /usr/local/bin/newUCSCdb.pl
$ podman run --it --rm --entrypoint /usr/local/bin/newUCSCdb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/newUCSCdb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize_multicov.pl

```bash
$ singularity exec <container> /usr/local/bin/normalize_multicov.pl
$ podman run --it --rm --entrypoint /usr/local/bin/normalize_multicov.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize_multicov.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaseq_peakfinder.pl

```bash
$ singularity exec <container> /usr/local/bin/rnaseq_peakfinder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnaseq_peakfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaseq_peakfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sj_visualizer.pl

```bash
$ singularity exec <container> /usr/local/bin/sj_visualizer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sj_visualizer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sj_visualizer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splice_site_summary.pl

```bash
$ singularity exec <container> /usr/local/bin/splice_site_summary.pl
$ podman run --it --rm --entrypoint /usr/local/bin/splice_site_summary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splice_site_summary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### track_hub_constructor.pl

```bash
$ singularity exec <container> /usr/local/bin/track_hub_constructor.pl
$ podman run --it --rm --entrypoint /usr/local/bin/track_hub_constructor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/track_hub_constructor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_fastq.pl

```bash
$ singularity exec <container> /usr/local/bin/trim_fastq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/trim_fastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_fastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pod_cover

```bash
$ singularity exec <container> /usr/local/bin/pod_cover
$ podman run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedGraphToBigWig

```bash
$ singularity exec <container> /usr/local/bin/bedGraphToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBigBed

```bash
$ singularity exec <container> /usr/local/bin/bedToBigBed
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToTwoBit

```bash
$ singularity exec <container> /usr/local/bin/faToTwoBit
$ podman run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifecho

```bash
$ singularity exec <container> /usr/local/bin/gifecho
$ podman run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifinto

```bash
$ singularity exec <container> /usr/local/bin/gifinto
$ podman run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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