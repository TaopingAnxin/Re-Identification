import scipy.io
import matplotlib.pyplot as plt
import numpy as np

def visualize_event_data(mat_file_path, save_path=None):
    # Load .mat file
    data = scipy.io.loadmat(mat_file_path)
    
    # Extract the information from the events
    x = data['section_event_x'].flatten().astype(np.int32)
    y = data['section_event_y'].flatten().astype(np.int32)
    polarity = data['section_event_polarity'].flatten().astype(np.int32)  # 1 for positive events, 0 for negative events
    
    # Create a black background image
    height, width = np.max(y) + 1, np.max(x) + 1
    event_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Set positive events to red and negative events to green
    event_image[y[polarity == 1], x[polarity == 1], 0] = 255  # Red channel for positive events
    event_image[y[polarity == 0], x[polarity == 0], 1] = 255  # Green channel for negative events

    # Plot the event image
    plt.figure(figsize=(10, 10))
    plt.imshow(event_image)
    plt.title('Event Data Visualization')
    plt.axis('off')  # Hide axis
    
    # Save the image if save_path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

# Example usage
mat_file_path = '/home/pingpai/mnt_10T/ste-net/ste-net-master/data/PRID/prid_2011_event/cam_b/person_0078/001.mat'
save_path = 'event_data_visualization.png'
visualize_event_data(mat_file_path, save_path)