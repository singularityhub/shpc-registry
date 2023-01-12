---
layout: container
name:  "quay.io/biocontainers/rgt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rgt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rgt/container.yaml"
updated_at: "2023-01-12 03:53:27.160862"
latest: "0.12.3--py27h2b63b92_3"
container_url: "https://biocontainers.pro/tools/rgt"
aliases:
 - "bed2associated_genes.py"
 - "bed2fasta.py"
 - "bigBedToBed"
 - "bigWigMerge"
 - "download-db.sh"
 - "emtools.py"
 - "expressionFromGenomicSet.py"
 - "geneAssociationZscore.py"
 - "geneOntologyFromBed.py"
 - "genesFromBed.py"
 - "havana_analysis.py"
 - "intersectGenomicSets.py"
 - "mapExpressionMotif.py"
 - "mapGeneNetwork.py"
 - "moods-dna.py"
 - "phylocsf_check.py"
 - "protectionScore.py"
 - "random_regions.py"
 - "rgt-TDF"
 - "rgt-THOR"
 - "rgt-filterVCF"
 - "rgt-hint"
 - "rgt-motifanalysis"
 - "rgt-tools.py"
 - "rgt-viz"
 - "setupGenomicData.py"
 - "setupLogoData.py"
 - "update_alias.py"
 - "wigToBigWig"
 - "bedGraphToBigWig"
 - "htseq-count"
 - "htseq-qa"
 - "bedToBigBed"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "natsort"
 - "my_print_defaults"
versions:
 - "0.12.3--py27h2b63b92_3"
description: "shpc-registry automated BioContainers addition for rgt"
config: {"url": "https://biocontainers.pro/tools/rgt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rgt", "latest": {"0.12.3--py27h2b63b92_3": "sha256:3ba10a56cba8ad89aad24d2b79e8e8954456984456a86e2d9cb59dff6cf98dd3"}, "tags": {"0.12.3--py27h2b63b92_3": "sha256:3ba10a56cba8ad89aad24d2b79e8e8954456984456a86e2d9cb59dff6cf98dd3"}, "docker": "quay.io/biocontainers/rgt", "aliases": {"bed2associated_genes.py": "/usr/local/bin/bed2associated_genes.py", "bed2fasta.py": "/usr/local/bin/bed2fasta.py", "bigBedToBed": "/usr/local/bin/bigBedToBed", "bigWigMerge": "/usr/local/bin/bigWigMerge", "download-db.sh": "/usr/local/bin/download-db.sh", "emtools.py": "/usr/local/bin/emtools.py", "expressionFromGenomicSet.py": "/usr/local/bin/expressionFromGenomicSet.py", "geneAssociationZscore.py": "/usr/local/bin/geneAssociationZscore.py", "geneOntologyFromBed.py": "/usr/local/bin/geneOntologyFromBed.py", "genesFromBed.py": "/usr/local/bin/genesFromBed.py", "havana_analysis.py": "/usr/local/bin/havana_analysis.py", "intersectGenomicSets.py": "/usr/local/bin/intersectGenomicSets.py", "mapExpressionMotif.py": "/usr/local/bin/mapExpressionMotif.py", "mapGeneNetwork.py": "/usr/local/bin/mapGeneNetwork.py", "moods-dna.py": "/usr/local/bin/moods-dna.py", "phylocsf_check.py": "/usr/local/bin/phylocsf_check.py", "protectionScore.py": "/usr/local/bin/protectionScore.py", "random_regions.py": "/usr/local/bin/random_regions.py", "rgt-TDF": "/usr/local/bin/rgt-TDF", "rgt-THOR": "/usr/local/bin/rgt-THOR", "rgt-filterVCF": "/usr/local/bin/rgt-filterVCF", "rgt-hint": "/usr/local/bin/rgt-hint", "rgt-motifanalysis": "/usr/local/bin/rgt-motifanalysis", "rgt-tools.py": "/usr/local/bin/rgt-tools.py", "rgt-viz": "/usr/local/bin/rgt-viz", "setupGenomicData.py": "/usr/local/bin/setupGenomicData.py", "setupLogoData.py": "/usr/local/bin/setupLogoData.py", "update_alias.py": "/usr/local/bin/update_alias.py", "wigToBigWig": "/usr/local/bin/wigToBigWig", "bedGraphToBigWig": "/usr/local/bin/bedGraphToBigWig", "htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "bedToBigBed": "/usr/local/bin/bedToBigBed", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "natsort": "/usr/local/bin/natsort", "my_print_defaults": "/usr/local/bin/my_print_defaults"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rgt.
shpc-registry automated BioContainers addition for rgt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rgt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rgt:0.12.3--py27h2b63b92_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rgt/0.12.3--py27h2b63b92_3
$ module help quay.io/biocontainers/rgt/0.12.3--py27h2b63b92_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rgt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rgt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rgt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rgt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rgt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rgt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bed2associated_genes.py

```bash
$ singularity exec <container> /usr/local/bin/bed2associated_genes.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed2associated_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2associated_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2fasta.py

```bash
$ singularity exec <container> /usr/local/bin/bed2fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/bed2fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigBedToBed

```bash
$ singularity exec <container> /usr/local/bin/bigBedToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bigBedToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigBedToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigMerge

```bash
$ singularity exec <container> /usr/local/bin/bigWigMerge
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigMerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigMerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-db.sh

```bash
$ singularity exec <container> /usr/local/bin/download-db.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emtools.py

```bash
$ singularity exec <container> /usr/local/bin/emtools.py
$ podman run --it --rm --entrypoint /usr/local/bin/emtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/emtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### expressionFromGenomicSet.py

```bash
$ singularity exec <container> /usr/local/bin/expressionFromGenomicSet.py
$ podman run --it --rm --entrypoint /usr/local/bin/expressionFromGenomicSet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/expressionFromGenomicSet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geneAssociationZscore.py

```bash
$ singularity exec <container> /usr/local/bin/geneAssociationZscore.py
$ podman run --it --rm --entrypoint /usr/local/bin/geneAssociationZscore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geneAssociationZscore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geneOntologyFromBed.py

```bash
$ singularity exec <container> /usr/local/bin/geneOntologyFromBed.py
$ podman run --it --rm --entrypoint /usr/local/bin/geneOntologyFromBed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geneOntologyFromBed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genesFromBed.py

```bash
$ singularity exec <container> /usr/local/bin/genesFromBed.py
$ podman run --it --rm --entrypoint /usr/local/bin/genesFromBed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genesFromBed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### havana_analysis.py

```bash
$ singularity exec <container> /usr/local/bin/havana_analysis.py
$ podman run --it --rm --entrypoint /usr/local/bin/havana_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/havana_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersectGenomicSets.py

```bash
$ singularity exec <container> /usr/local/bin/intersectGenomicSets.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersectGenomicSets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersectGenomicSets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapExpressionMotif.py

```bash
$ singularity exec <container> /usr/local/bin/mapExpressionMotif.py
$ podman run --it --rm --entrypoint /usr/local/bin/mapExpressionMotif.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapExpressionMotif.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapGeneNetwork.py

```bash
$ singularity exec <container> /usr/local/bin/mapGeneNetwork.py
$ podman run --it --rm --entrypoint /usr/local/bin/mapGeneNetwork.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapGeneNetwork.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moods-dna.py

```bash
$ singularity exec <container> /usr/local/bin/moods-dna.py
$ podman run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylocsf_check.py

```bash
$ singularity exec <container> /usr/local/bin/phylocsf_check.py
$ podman run --it --rm --entrypoint /usr/local/bin/phylocsf_check.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylocsf_check.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protectionScore.py

```bash
$ singularity exec <container> /usr/local/bin/protectionScore.py
$ podman run --it --rm --entrypoint /usr/local/bin/protectionScore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protectionScore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### random_regions.py

```bash
$ singularity exec <container> /usr/local/bin/random_regions.py
$ podman run --it --rm --entrypoint /usr/local/bin/random_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/random_regions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgt-TDF

```bash
$ singularity exec <container> /usr/local/bin/rgt-TDF
$ podman run --it --rm --entrypoint /usr/local/bin/rgt-TDF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgt-TDF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgt-THOR

```bash
$ singularity exec <container> /usr/local/bin/rgt-THOR
$ podman run --it --rm --entrypoint /usr/local/bin/rgt-THOR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgt-THOR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgt-filterVCF

```bash
$ singularity exec <container> /usr/local/bin/rgt-filterVCF
$ podman run --it --rm --entrypoint /usr/local/bin/rgt-filterVCF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgt-filterVCF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgt-hint

```bash
$ singularity exec <container> /usr/local/bin/rgt-hint
$ podman run --it --rm --entrypoint /usr/local/bin/rgt-hint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgt-hint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgt-motifanalysis

```bash
$ singularity exec <container> /usr/local/bin/rgt-motifanalysis
$ podman run --it --rm --entrypoint /usr/local/bin/rgt-motifanalysis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgt-motifanalysis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgt-tools.py

```bash
$ singularity exec <container> /usr/local/bin/rgt-tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/rgt-tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgt-tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgt-viz

```bash
$ singularity exec <container> /usr/local/bin/rgt-viz
$ podman run --it --rm --entrypoint /usr/local/bin/rgt-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgt-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setupGenomicData.py

```bash
$ singularity exec <container> /usr/local/bin/setupGenomicData.py
$ podman run --it --rm --entrypoint /usr/local/bin/setupGenomicData.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setupGenomicData.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setupLogoData.py

```bash
$ singularity exec <container> /usr/local/bin/setupLogoData.py
$ podman run --it --rm --entrypoint /usr/local/bin/setupLogoData.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setupLogoData.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_alias.py

```bash
$ singularity exec <container> /usr/local/bin/update_alias.py
$ podman run --it --rm --entrypoint /usr/local/bin/update_alias.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_alias.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigToBigWig

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedGraphToBigWig

```bash
$ singularity exec <container> /usr/local/bin/bedGraphToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count

```bash
$ singularity exec <container> /usr/local/bin/htseq-count
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-qa

```bash
$ singularity exec <container> /usr/local/bin/htseq-qa
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBigBed

```bash
$ singularity exec <container> /usr/local/bin/bedToBigBed
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
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