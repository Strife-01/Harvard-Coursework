// Modifies the volume of an audio file

#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    uint8_t buffer_header;
    int header_index = 0;
    while(header_index < HEADER_SIZE && fread(&buffer_header, sizeof(buffer_header), 1, input))
    {
        fwrite(&buffer_header, sizeof(buffer_header), 1, output);
        header_index++;
    }

    // TODO: Read samples from input file and write updated data to output file
    int16_t volume_sample;
    while (fread(&volume_sample, sizeof(volume_sample), 1, input))
    {
        volume_sample *= factor;
        fwrite(&volume_sample, sizeof(volume_sample), 1, output);
    }


    // Close files
    fclose(input);
    fclose(output);
}
