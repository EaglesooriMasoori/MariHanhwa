//
//  DetailViewController.h
//  MariHanhwa
//
//  Created by Rapael Lee on 10/14/15.
//  Copyright © 2015 mazicloud. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DetailViewController : UIViewController

@property (strong, nonatomic) id detailItem;
@property (weak, nonatomic) IBOutlet UILabel *detailDescriptionLabel;

@end

