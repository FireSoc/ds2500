'''mounting in colab:
 from google.colab import drive
 drive.mount("/content/drive")'''
def np_in_lst(ray1,ray2,m):
    np_ray1 = (ray1)
    np_ray2 = (ray2)
    c = np_ray1 * np_ray2 * m
    lst = [c(i) for i in range(len(c))]
    return lst

print(np_in_lst([1,2,3], [1,2,3], 10))