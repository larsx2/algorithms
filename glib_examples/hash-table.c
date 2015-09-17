#include <stdio.h>
#include <glib.h>

int main() {
    GHashTable * hash = g_hash_table_new(g_str_hash, g_str_equal);

    g_hash_table_insert(hash, "Virginia", "Richmod");
    g_hash_table_insert(hash, "Texas", "Austin");
    g_hash_table_insert(hash, "Ohio", "Columbus");

    printf("There are %d keys in the hash\n", g_hash_table_size(hash));
    printf("The capital of Texas is %s\n", 
               (char *)g_hash_table_lookup(hash, "Texas"));

    gboolean found = g_hash_table_remove(hash, "Virginia");
    printf("The value `Virginia` was %sfound and removed\n", 
               found ? "":"not");
    printf("There are %d keys in the hash now\n", g_hash_table_size(hash));

    g_hash_table_destroy(hash);

    return 0;
}
